--juan elias lara soto
--examen 2024 junio
--administracion de base de datos


CREATE TABLE centro (
   id     NUMBER PRIMARY KEY,
   nombre VARCHAR2(100)
);

CREATE TABLE entrenador (
   id            NUMBER PRIMARY KEY,
   nombre        VARCHAR2(100),
   centro        NUMBER,
   num_clientes  NUMBER DEFAULT 0,
   FOREIGN KEY (centro) REFERENCES centro(id)
);

CREATE TABLE cliente (
   id       NUMBER PRIMARY KEY,
   nombre   VARCHAR2(100)
);

CREATE TABLE entrena (
   cliente_id     NUMBER,
   entrenador_id  NUMBER,
   PRIMARY KEY (cliente_id, entrenador_id),
   FOREIGN KEY (cliente_id) REFERENCES cliente(id),
   FOREIGN KEY (entrenador_id) REFERENCES entrenador(id)
);

--EJERCICIO 1

CREATE OR REPLACE FUNCTION calcula_num_clientes (
   a_codigo IN NUMBER
) RETURN NUMBER IS
   v_cant NUMBER;
BEGIN
   SELECT COUNT(*) INTO v_cant
   FROM entrena
   WHERE entrenador_id = a_codigo;

   RETURN v_cant;
END;
/

--EJERCICIO 2
CREATE OR REPLACE PROCEDURE calcula_clientes_centro (
   a_codigo_centro IN NUMBER
) IS
   CURSOR cur IS
      SELECT id FROM entrenador
      WHERE centro = a_codigo_centro
      FOR UPDATE;

   v_cant NUMBER;
BEGIN
   FOR c IN cur LOOP
      v_cant := calcula_num_clientes(c.id);
      UPDATE entrenador
      SET num_clientes = v_cant
      WHERE id = c.id;
   END LOOP;

   COMMIT;
END;
/

--EJERCICIO 3
CREATE OR REPLACE TRIGGER tr_num_clientes
BEFORE INSERT OR DELETE OR UPDATE ON entrena
FOR EACH ROW
BEGIN
   IF INSERTING THEN
      UPDATE entrenador 
      SET num_clientes = num_clientes + 1
      WHERE id = :new.entrenador_id;

   ELSIF DELETING THEN
      UPDATE entrenador 
      SET num_clientes = num_clientes - 1
      WHERE id = :old.entrenador_id;

   ELSIF UPDATING THEN
      IF :old.entrenador_id != :new.entrenador_id THEN
         UPDATE entrenador 
         SET num_clientes = num_clientes + 1
         WHERE id = :new.entrenador_id;

         UPDATE entrenador 
         SET num_clientes = num_clientes - 1
         WHERE id = :old.entrenador_id;
      END IF;
   END IF;
END;
/

--EJERCICIO 4
create or replace procedure crea_vista_entrenador(codigo in number) is 
sentencia varchar2(1000);
begin
sentencia:= 'create view v_entrenador_'||codigo||' (e_nombre, e_apellidos, c_nombre, c_apellidos) 
as  
select u1.nombre, u1.apellidos, u2.nombre, u2.apellidos 
from entrenador e join usuario u1 on (u1.id = e.id) left join  
entrena en on e.id = en.entrenador_id  
left join cliente c on en.cliente_id = c.id 
left join usuario u2 on c.id = u2.id 
where e.id =' ||codigo||';';
DBMS_OUTPUT.PUT_LINE (Sentencia); 
execute immediate(sentencia);
end;

--EJERCICIO 5
create or replace procedure borra_vista_entrenador (p_entrenador ENTRENADOR.ID%TYPE) is 
sentencia varchar2(100);
begin 
sentencia :='drop view v_entrenador'||p_entrenador;
dbms_output.put_line(sentencia);
execute immediate sentencia;
end;
--EJERCICIO 6
create or replace PACKAGE PK_EXAMEN24 AS  
procedure CREA_VISTAS_CENTRO (p_centro centro.id%type); 
END PK_EXAMEN24; 


create or replace PACKAGE BODY PK_EXAMEN24 AS 
procedure CREA_VISTAS_CENTRO (p_centro centro.id%type) AS 
cursor c_centro is select id from entrenador  
where centro_id = p_centro; 
num number; 
BEGIN 
select count(*) into num from centro where id = p_centro; 
if num = 0 then  
raise esc.pk_prueba_examen.CENTRO_NO_EXISTE; 
else     
for v in c_centro loop 
begin 
borra_vista_entrenador (v.id); 
exception when others then null; 
end; 
begin 
crea_vista_entrenador (v.id); 
exception when others then null; 
end; 
end loop; 
end if; 
END CREA_VISTAS_CENTRO; 
END PK_EXAMEN24; 

