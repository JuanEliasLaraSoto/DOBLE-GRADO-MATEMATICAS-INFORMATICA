--EXAMEN JUNIO 2023
--ADMINISTRACION DE BASE DE DATOS
--JUAN ELIAS LARA SOTO

-- Tabla SEDE
CREATE TABLE sede (
    codigo    VARCHAR2(10) PRIMARY KEY,
    nombre    VARCHAR2(100),
    direccion VARCHAR2(200)
);

-- Tabla CENTRO
CREATE TABLE centro (
    nombre    VARCHAR2(100) PRIMARY KEY,
    sede      VARCHAR2(10) REFERENCES sede(codigo),
    capacidad NUMBER
);

-- Tabla ESTUDIANTE
CREATE TABLE estudiante (
    dni     VARCHAR2(20) PRIMARY KEY,
    nombre  VARCHAR2(100),
    centro  VARCHAR2(100) REFERENCES centro(nombre)
);

-- Tabla MATERIA
CREATE TABLE materia (
    codigo  VARCHAR2(20) PRIMARY KEY,
    nombre  VARCHAR2(100),
    fecha   DATE
);

-- Tabla MATRICULA
CREATE TABLE matricula (
    dni     VARCHAR2(20) REFERENCES estudiante(dni),
    materia VARCHAR2(20) REFERENCES materia(codigo),
    PRIMARY KEY (dni, materia)
);

-- ============================
-- TABLAS A CREAR EN TU ESQUEMA
-- ============================

-- Tabla AULA
CREATE TABLE aula (
    sede              VARCHAR2(20),
    codigo            VARCHAR2(20),
    capacidad         NUMBER,
    capacidad_examen  NUMBER,
    PRIMARY KEY (sede, codigo)
);

-- Tabla ASISTENCIA
CREATE TABLE asistencia (
    sede     VARCHAR2(20),
    materia  VARCHAR2(20),
    aula     VARCHAR2(20),
    fecha    DATE,
    dni      VARCHAR2(20),
    asiste   CHAR(1),
    entrega  CHAR(1),
    PRIMARY KEY (sede, materia, aula, fecha, dni)
);

--EJERCICIO 1
create or replace trigger tr_comprueba_capacidad before  insert or update  on aula for each row
begin 
if not (:new.capacidad_examen>0 and :new.capacidad_examen <:new.capacidad) then 
raise SIMEX32CE47.PK_EXCEPCIONES.CAPACIDAD_INCORRECTA;
end if;
end ;
/

--EJERCICIO 2
create or replace procedure nueva_aula (a_sede in varchar2,a_codigo in varchar2 , a_capacidad in number ,a_capacidad_examen in number) is
v_cant number;
begin 
select count (*) into v_cant from aulas where sede=a_sede and codigo=a_codigo;
if v_cant =0 then
insert into aulas (sede,codigo,capacidad,capacidad_examen) values (a_sede,a_codigo,a_capacidad,a_capacidad_examen);
commit;
elsif v_cant>0  then 
update aulas set capacidad=a_capacidad, capacidad_examen=a_capacidad_examen where sede=a_sede and codigo=a_codigo;
commit;
end if;
end;
/
--EJERCICIO 3
create or replace procedure crear_aulas (a_sede in varchar2,a_capacidad in number ,a_capacidad_examen in number) is
cursor cur is select nombre from centros  where sede=a_sede and capacidad=a_capacidad;
begin 
for c in cur loop 
nueva_aula ( a_sede, SUBSTR(c.nombre,8,8),a_capacidad,a_capacidad_examen);
end loop;
end;
/
--EJERCICIO 4
create or replace procedure borra_aulas(p_sede varchar2)
is
v_count number; 
begin 
select count(*) into v_count from asistencia where sede=p_sede;
if v_count =0 then
delete from aulas where sede=p_sede;
else 
delete from aulas where sede=p_sede;
delete from asistencia where sede=p_sede;
commit;
end if;
end;
/

--EJERCICIO 5 
CREATE OR REPLACE PROCEDURE insertar_asistencia (
   p_sede     IN VARCHAR2,
   p_materia  IN VARCHAR2,
   p_aula     IN VARCHAR2,
   p_fecha    IN DATE,
   p_dni      IN VARCHAR2
) IS
   v_count NUMBER;
BEGIN
   -- Verificamos si existe el aula con ese código en esa sede
   SELECT COUNT(*) INTO v_count
   FROM aula
   WHERE sede = p_sede AND codigo = p_aula;

   IF v_count = 0 THEN
      RAISE SIMEX32CE47.PK_EXCEPCIONES.AULA_INCORRECTA;
   END IF;

   -- Insertamos la asistencia con asiste y entrega a NULL
   INSERT INTO asistencia (
      sede, materia, aula, fecha, dni, asiste, entrega
   ) VALUES (
      p_sede, p_materia, p_aula, p_fecha, p_dni, NULL, NULL
   );

   COMMIT;
END;
/


--EJERCICIO 6
-- ESPECIFICACIÓN DEL PAQUETE
CREATE OR REPLACE PACKAGE pk_examen23 IS
   FUNCTION fecha_materia(p_codigo VARCHAR2) RETURN DATE;
   PROCEDURE reparte(p_sede VARCHAR2, p_materia VARCHAR2);
END pk_examen23;
/
-- CUERPO DEL PAQUETE
CREATE OR REPLACE PACKAGE BODY pk_examen23 IS

   FUNCTION fecha_materia(p_codigo VARCHAR2) RETURN DATE IS
      v_fecha DATE;
   BEGIN
      SELECT fecha INTO v_fecha
      FROM materia
      WHERE codigo = p_codigo;

      RETURN v_fecha;

   EXCEPTION
      WHEN NO_DATA_FOUND THEN
         RETURN SYSDATE;
   END fecha_materia;

   PROCEDURE reparte(p_sede VARCHAR2, p_materia VARCHAR2) IS
      CURSOR c_centros IS
         SELECT nombre FROM centro WHERE sede = p_sede;

      CURSOR c_estudiantes(v_centro_nombre VARCHAR2) IS
         SELECT e.dni
         FROM estudiante e
         JOIN matricula m ON e.dni = m.dni
         WHERE e.centro = v_centro_nombre
           AND m.materia = p_materia;

      v_codigo_aula  VARCHAR2(20);
      v_fecha        DATE;
      v_capacidad    NUMBER;
      v_ocupacion    NUMBER;

   BEGIN
      v_fecha := fecha_materia(p_materia);  -- función del ejercicio 6

      FOR c IN c_centros LOOP
         BEGIN
            -- Obtener el código del aula a partir del nombre del centro
            v_codigo_aula := SUBSTR(c.nombre, 8, 8);

            -- Comprobar existencia del aula y obtener su capacidad
            SELECT capacidad_examen INTO v_capacidad
            FROM aula
            WHERE sede = p_sede AND codigo = v_codigo_aula;

            -- Consultar ocupación actual del aula
            SELECT COUNT(*) INTO v_ocupacion
            FROM asistencia
            WHERE sede = p_sede AND aula = v_codigo_aula;

            -- Si hay aforo disponible
            IF v_ocupacion < v_capacidad THEN
               FOR est IN c_estudiantes(c.nombre) LOOP
                  BEGIN
                     insertar_asistencia(
                        p_sede,
                        p_materia,
                        v_codigo_aula,
                        v_fecha,
                        est.dni
                     );
                  EXCEPTION
                     WHEN OTHERS THEN
                        RAISE SIMEX32CE47.PK_EXCEPCIONES.reparto_incorrecto;
                  END;
               END LOOP;
            END IF;

         EXCEPTION
            WHEN NO_DATA_FOUND THEN
               RAISE SIMEX32CE47.PK_EXCEPCIONES.reparto_incorrecto;
            WHEN OTHERS THEN
               RAISE SIMEX32CE47.PK_EXCEPCIONES.reparto_incorrecto;
         END;
      END LOOP;
   END reparte;

END pk_examen23;
/
