SELECT * FROM all_TABLES;
--ejercicio 1
CREATE TABLE libros (
    id_libro         NUMBER PRIMARY KEY,
    titulo           VARCHAR2(150),
    autor            VARCHAR2(100),
    fecha_publicacion DATE,
    genero           VARCHAR2(50),
    precio           NUMBER(6, 2)
);

CREATE TABLE RECETAS (
    id         NUMBER PRIMARY KEY,
    titulo           VARCHAR2(150),
    autor            VARCHAR2(100),
    fecha_publicacion DATE
);
set serveroutput on;


 DECLARE
 v_table_name VARCHAR2(100);
 v_owner VARCHAR2(100) := USER;
 CURSOR c_tables IS SELECT table_name FROM user_tables;
 BEGIN
 FOR table_rec IN c_tables LOOP
 v_table_name := table_rec.table_name;
 DBMS_OUTPUT.PUT_LINE('La tabla ' || v_table_name || ' pertenece al esquema ' || v_owner);
 END LOOP;
 END;
 /
 
--ejercicio 2
 DECLARE
 v_table_name VARCHAR2(100);
 v_owner VARCHAR2(100) ;
 CURSOR c_tables IS SELECT table_name,owner FROM all_tables where owner!=user;
 BEGIN
 FOR table_rec IN c_tables LOOP
 v_table_name := table_rec.table_name;
 v_owner := table_rec.owner;
 DBMS_OUTPUT.PUT_LINE('La tabla ' || v_table_name || ' pertenece al esquema ' || v_owner);
 END LOOP;
 END;
 /
 
 --EJERCICIO 3
 --HE MODIFICADO LA SENTICIA DEL SELECT Y ADEMAS HE AÑADIDO LA CONDICION OWNER !=USER PARA QUE SE OBSERVEN SOLO LAS TABLAS A LAS QUE TENGO ACCESO Y NO LAS MÍAS

--EJERCICIO 4  
--EN EL PRIMER EJERCICIO NO SE NECESITA CREAR EL CURSOR SELECCIONANDO EL OWNER PQ SOLO HAY UN OWNER Y SOY YO MISMO
--EN EL SEGUNDO SI HACE FALTA, YA QUE HAY MUCHOS OWNER, TODOS AQUELLOS A LOS QUE TENGO ACCESO PARA ACCEDER A SUS TABLAS.

--EJERCICIO 5
CREATE OR REPLACE PROCEDURE RECORRE_TABLAS(P_MODE IN NUMBER DEFAULT NULL) IS
    -- Cursor sobre ALL_TABLES con filtro condicional
    CURSOR c_tablas IS
        SELECT owner, table_name
        FROM all_tables
        WHERE DECODE(NVL(P_MODE, -1), 0, 1, DECODE(owner, USER, 1, 0)) = 1;--SELECCIONA SEGUN SI OWNER COMPLE CON LO DE P_MODE
BEGIN
    IF P_MODE IS NULL THEN
        DBMS_OUTPUT.PUT_LINE('Uso del procedimiento RECORRE_TABLAS(P_MODE):');
        DBMS_OUTPUT.PUT_LINE('   - P_MODE = 0: muestra todas las tablas a las que tiene acceso el usuario.');
        DBMS_OUTPUT.PUT_LINE('   - P_MODE != 0: muestra solo las tablas propias del usuario.');
        RETURN;
    END IF;

    FOR t IN c_tablas LOOP
        DBMS_OUTPUT.PUT_LINE('La tabla ' || t.table_name || ' pertenece al esquema ' || t.owner);
    END LOOP;
END;
/
