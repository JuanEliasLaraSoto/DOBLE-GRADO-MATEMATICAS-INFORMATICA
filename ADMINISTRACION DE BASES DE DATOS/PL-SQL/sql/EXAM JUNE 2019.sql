--JUAN ELIAS LARA SOTO
--ADMINISTRACION DE BASE DE DATOS
--EXAMEN JUNIO 2019


-- Tabla EMPLEADO
CREATE TABLE EMPLEADO (
  ID         NUMBER PRIMARY KEY,
  DNI        VARCHAR2(10),
  NOMBRE     VARCHAR2(50),
  APELLIDO1  VARCHAR2(50),
  APELLIDO2  VARCHAR2(50),
  CATEGORIA  NUMBER,
  USUARIO    VARCHAR2(30)
);

-- Tabla NOMINA
CREATE TABLE NOMINA (
  EMPLEADO       NUMBER NOT NULL,
  FECHA_EMISION  DATE,
  IMPORTE_NETO   NUMBER,
  IMPORTE_BRUTO  NUMBER,
  CONSTRAINT PK_NOMINA PRIMARY KEY (EMPLEADO, FECHA_EMISION),
  CONSTRAINT FK_NOMINA_EMPLEADO FOREIGN KEY (EMPLEADO)
    REFERENCES EMPLEADO(ID)
);

-- Tabla CONTROL_NOMINA
CREATE TABLE CONTROL_NOMINA (
  FECHA     DATE NOT NULL,
  USUARIO   VARCHAR2(35),
  EMPLEADO  NUMBER NOT NULL,
  ANTES     NUMBER,
  DESPUES   NUMBER,
  CONSTRAINT FK_CONTROL_EMPLEADO FOREIGN KEY (EMPLEADO)
    REFERENCES EMPLEADO(ID)
);

--EJERCICIO 1
create or replace trigger tr_nomina before insert or update on nomina for each row
begin
if updating then
insert into control_nomina (fecha,usuario,empleado,antes,despues) values (sysdate,user,:new.empleado,:old.importe_bruto, :new.importe_bruto);
elsif inserting then 
insert into control_nomina (fecha,usuario,empleado,antes,despues) values (sysdate,user,:new.empleado,null, :new.importe_bruto);
end if;
end;

CREATE OR REPLACE PACKAGE PK_NOMINAS AS 
PROCEDURE P_CREA_NOMINA (FECHA_ACTUAL DATE, MES VARCHAR2); 
PROCEDURE P_BORRA_NOMINA (MES VARCHAR2); 
PROCEDURE P_VISTAS_EMPLEADOS (Categoria Number); 
END;
/
CREATE OR REPLACE PACKAGE BODY PK_NOMINAS IS

  PROCEDURE P_CREA_NOMINA (FECHA_ACTUAL DATE, MES VARCHAR2) IS
    CURSOR cur IS
      SELECT EMPLEADO, IMPORTE_NETO, IMPORTE_BRUTO
      FROM NOMINA
      WHERE TO_CHAR(FECHA_EMISION, 'MM/YYYY') = MES;
  BEGIN
    FOR c IN cur LOOP
      INSERT INTO NOMINA (EMPLEADO, FECHA_EMISION, IMPORTE_NETO, IMPORTE_BRUTO)
      VALUES (c.EMPLEADO, FECHA_ACTUAL, c.IMPORTE_NETO, c.IMPORTE_BRUTO);
    END LOOP;
    commit;
  END P_CREA_NOMINA;




procedure p_borra_nomina (mes varchar2) is 
begin
delete from nomina where TO_CHAR(fecha_emision, 'mm/yyyy')= mes;
COMMIT;
end;

PROCEDURE P_VISTAS_EMPLEADOS (v_Categoria Number) is
cursor cur is select id,usuario from empleado where categoria=v_categoria;
sentencia varchar2(1000);
begin 
for c in cur loop
begin
sentencia:= 'CREATE OR REPLACE VIEW '|| c.usuario||'_NOMINA AS SELECT DNI, NOMBRE, APELLIDO1, 
APELLIDO2, FECHA_EMISION, IMPORTE_NETO, IMPORTE_BRUTO FROM EMPLEADO E JOIN 
NOMINA N ON E.ID = N.EMPLEADO WHERE E.ID ='||c.id ;
dbms_output.put_line(sentencia);
execute immediate(sentencia);
commit;
exception 
when others then DBMS_OUTPUT.PUT_LINE('Error al crear vista para ' || c.usuario || ': ' || SQLERRM);
end;
end loop;
end;
end pk_nominas;
/
 BEGIN
 PK_NOMINAS.P_CREA_NOMINA('16/06/2025','06/2024');
 END;
 BEGIN
 PK_NOMINAS.P_BORRA_NOMINA('05/2024');
 END;

 BEGIN
 PK_NOMINAS.P_VISTAS_EMPLEADOS(4);
 END;