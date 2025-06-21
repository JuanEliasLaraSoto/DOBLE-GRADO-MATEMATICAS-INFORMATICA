
--ADMINISTRACION BASE DE DATOS 
--EXAMEN SEPTIEMBRE 2022
--JUAN ELAIS LARA SOTO

create table socios (
numero varchar2(16) primary key,
nombre varchar2(50) not null,
telefono varchar2(16) not null);

create table libros (
isbn varchar2(16) primary key, 
titulo varchar2(50) not null,
autor varchar2(16) not null,
cantidad number(3) not null);

create table prestamos (
numero varchar2(16) not null,
isbn varchar(16) not null,
inicio date not null,
fin date);

create table descatalogados (
isbn varchar2(16) not null,
fecha date not null);

-- Clave foránea desde PRESTAMOS(NUMERO) hacia SOCIOS(NUMERO)
ALTER TABLE PRESTAMOS
ADD CONSTRAINT FK_PRESTAMOS_SOCIOS
FOREIGN KEY (NUMERO)
REFERENCES SOCIOS(NUMERO);

-- Clave foránea desde PRESTAMOS(ISBN) hacia LIBROS(ISBN)
ALTER TABLE PRESTAMOS
ADD CONSTRAINT FK_PRESTAMOS_LIBROS
FOREIGN KEY (ISBN)
REFERENCES LIBROS(ISBN);

--EJERCICIO 1
create or replace trigger t_prestamo after insert on prestamos 
for each row  
begin 
if not(:new.fin is null or :new.fin>:new.inicio) then 
raise_application_error(-20502,
'Error: la fecha de fin debe ser posterior a la de inicio o estar vacía.');
 end if;
 end;
/
--EJERCICIO 2

create or replace trigger t_descatalogar before update on libros for each row 
declare 
v_cant number;
begin 
v_cant:= :old.cantidad-:new.cantidad;
if v_cant<0 then raise_application_error(-20500,
'Error: la cantidad no puede incrementarse. Solo se permite reducir.');

else 
for c in 1..v_cant loop
insert into descatalogados (isbn,fecha) values (:old.isbn, sysdate);
end loop;
commit;
end if;


end;
/
--EJERCICIO 3 
create or replace function f_prestamos (a_numero in varchar2, a_inicio in date,a_fin in date)
return number is 
v_cant NUMBER;
begin 
select count(*) into v_cant from prestamos where inicio between a_inicio and a_fin and a_numero=numero;
return v_cant;

end;
/
--EJERCICIO 4
create or replace procedure p_perdidos (a_fecha in date) is 
cursor cur is select numero,isbn from prestamos where fin is null and inicio <a_fecha;
begin
for  c in cur loop
update prestamos set fin=sysdate where c.numero=numero and c.isbn=isbn;
update libros set cantidad=cantidad-1 where c.isbn=isbn;

end loop;
commit;
end ;
/

--EJERCICIO 5

create or replace procedure p_forzado(a_numero in number, a_isbn in number, a_inicio in date, a_fin in date) is

begin 
insert into prestamos(numero,isbn,inicio,fin) values (a_numero,a_isbn,a_inicio,a_fin);
commit;

exception 
when others then 
insert into descatalogados(fecha,isbn) values (sysdate,a_isbn);
commit;

end;
/
