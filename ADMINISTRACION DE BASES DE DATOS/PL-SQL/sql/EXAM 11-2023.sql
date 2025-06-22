--JUAN ELAIS LARA SOTO
--ADMINISTRACION DE BASE DE DATOS
--EXAMEN DE 11/2023


--EJERCICIO 1
CREATE TABLE aula (  
codigo   number NOT NULL PRIMARY KEY,  
nombre    
VARCHAR2(32) NOT NULL UNIQUE,  
telefono  VARCHAR2(32) UNIQUE,  
capacidad NUMBER NOT NULL,  
borrado   CHAR(1) DEFAULT 'N' not null); 


CREATE VIEW v_aula AS SELECT codigo,nombre , telefono, capacidad  
FROM aula WHERE borrado = 'N'; 


create or replace trigger borra_aula  instead of delete on v_aula for each row
begin 
update aula set borrado='S' where codigo=:old.codigo;
end;

--EJERCICIO 2
create or replace package paq_renombra is
procedure renombra_uk(nombre in varchar2, nombre_clave in varchar2, nuevo_nombre in varchar2);
procedure renombra_todas_uk;
end paq_renombra;
/

create or replace package body paq_renombra is

procedure renombra_uk(nombre in varchar2, nombre_clave in varchar2, nuevo_nombre in varchar2) is
sentencia  varchar2(100);
begin
sentencia := 'ALTER TABLE ' || nombre ||
               ' RENAME CONSTRAINT ' || nombre_clave ||
               ' TO ' || nuevo_nombre;
execute immediate sentencia;
end;


 procedure renombra_todas_uk is
    CURSOR cur IS
      SELECT uc.table_name, uc.constraint_name, ucc.column_name
      FROM user_constraints uc
      JOIN user_cons_columns ucc ON uc.constraint_name = ucc.constraint_name
      WHERE uc.constraint_type = 'U';  -- solo claves únicasv_nuevo_nombre varchar2(100);
      V_NUEVO_NOMBRE VARCHAR2(50);
begin
for c in cur loop
v_nuevo_nombre:='UK_'||c.table_name||c.column_name;
renombra_uk(c.table_name,c.constraint_name ,v_nuevo_nombre);
end loop;
end;
end paq_renombra;
/
