-- Generado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   en:        2023-10-04 01:07:04 CEST
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE acto_piloto (
    acto_publico_fecha DATE NOT NULL,
    piloto_nombre      VARCHAR2(10 CHAR) NOT NULL
);

ALTER TABLE acto_piloto ADD CONSTRAINT acto_piloto_pk PRIMARY KEY ( acto_publico_fecha,
                                                                    piloto_nombre );

CREATE TABLE acto_publico (
    fecha            DATE NOT NULL,
    direccion        VARCHAR2(100 CHAR),
    descripcion      VARCHAR2(500 CHAR),
    numero_contacto  INTEGER,
    persona_contacto VARCHAR2(15)
);

ALTER TABLE acto_publico ADD CONSTRAINT acto_publico_pk PRIMARY KEY ( fecha );

CREATE TABLE carrera (
    tipo_neumatico_del  VARCHAR2(10 CHAR),
    tipo_neumatico_tras VARCHAR2(10),
    caida               INTEGER,
    tiempo              DATE,
    puntuacion          INTEGER,
    piloto_nombre       VARCHAR2(10 CHAR) NOT NULL,
    circuito_nombre     VARCHAR2(10 CHAR) NOT NULL
);

ALTER TABLE carrera ADD CONSTRAINT carrera_pk PRIMARY KEY ( piloto_nombre,
                                                            circuito_nombre );

CREATE TABLE circuito (
    nombre                    VARCHAR2(10 CHAR) NOT NULL,
    fecha                     DATE,
    pais                      VARCHAR2(15 CHAR),
    ciudad                    VARCHAR2(10 CHAR),
    ano_inaguracion           INTEGER,
    anchura                   NUMBER,
    posicion_parrilla         INTEGER,
    longitud_total            NUMBER,
    distancia_recta_mas_larga NUMBER,
    numero_curvas_izq         INTEGER,
    numero_curvas_der         INTEGER,
    mapa                      VARCHAR2(15 CHAR),
    numero_vueltas            INTEGER,
    tipo_carrera              VARCHAR2(10 CHAR)
);

ALTER TABLE circuito ADD CONSTRAINT circuito_pk PRIMARY KEY ( nombre );

ALTER TABLE circuito ADD CONSTRAINT circuito_fecha_un UNIQUE ( fecha );

CREATE TABLE empleado (
    codigo           INTEGER NOT NULL,
    pasaporte        VARCHAR2(15 CHAR),
    nacionalidad     VARCHAR2(10 CHAR),
    equipo_nombre    VARCHAR2(15 CHAR),
    equipo_nombre2   VARCHAR2(15 CHAR),
    nombre           VARCHAR2(15),
    fecha_nacimiento DATE,
    equipo_nombre4   VARCHAR2(15 CHAR),
    equipo_nombre3   VARCHAR2(15 CHAR)
);

CREATE UNIQUE INDEX empleado__idx ON
    empleado (
        equipo_nombre
    ASC );

CREATE UNIQUE INDEX empleado__idxv1 ON
    empleado (
        equipo_nombre4
    ASC );

ALTER TABLE empleado ADD CONSTRAINT empleado_pk PRIMARY KEY ( codigo );

ALTER TABLE empleado ADD CONSTRAINT empleado_nacionalidad_un UNIQUE ( nacionalidad );

ALTER TABLE empleado ADD CONSTRAINT empleado_pasaporte_un UNIQUE ( pasaporte );

CREATE TABLE equipo (
    nombre           VARCHAR2(15 CHAR) NOT NULL,
    modelo_moto      VARCHAR2(15 CHAR),
    direccion_postal VARCHAR2(20 CHAR),
    direccion_web    VARCHAR2(30 CHAR),
    objetivos        VARCHAR2(200 CHAR),
    foto_oficial     BLOB,
    logo             BLOB,
    empleado_codigo  INTEGER,
    empleado_codigo2 INTEGER
);

CREATE UNIQUE INDEX equipo__idx ON
    equipo (
        empleado_codigo
    ASC );

CREATE UNIQUE INDEX equipo__idxv1 ON
    equipo (
        empleado_codigo2
    ASC );

ALTER TABLE equipo ADD CONSTRAINT equipo_pk PRIMARY KEY ( nombre );

CREATE TABLE oficial (
    nombre            VARCHAR2(15 CHAR) NOT NULL,
    presupuesto       NUMBER,
    ano_creacion      INTEGER,
    direccion_fabrica VARCHAR2(20 CHAR)
);

ALTER TABLE oficial ADD CONSTRAINT oficial_pk PRIMARY KEY ( nombre );

CREATE TABLE piloto (
    nombre        VARCHAR2(10 CHAR) NOT NULL,
    dorsal        INTEGER,
    pais          VARCHAR2(10 CHAR),
    ciudad        VARCHAR2(20 CHAR),
    peso          NUMBER,
    altura        NUMBER,
    video         BLOB,
    equipo_nombre VARCHAR2(15 CHAR) NOT NULL
);

ALTER TABLE piloto ADD CONSTRAINT piloto_pk PRIMARY KEY ( nombre );

ALTER TABLE piloto ADD CONSTRAINT piloto_dorsal_un UNIQUE ( dorsal );

CREATE TABLE pilotov2 (
    piloto_nombre  VARCHAR2(10 CHAR) NOT NULL,
    piloto_nombre1 VARCHAR2(10 CHAR) NOT NULL
);

ALTER TABLE pilotov2 ADD CONSTRAINT pilotov1_pk PRIMARY KEY ( piloto_nombre,
                                                              piloto_nombre1 );

CREATE TABLE tiempos (
    vuelta                INTEGER NOT NULL,
    tiempo                DATE,
    piloto_nombre         VARCHAR2(10 CHAR) NOT NULL,
    tramo_codigo          INTEGER NOT NULL,
    tramo_circuito_nombre VARCHAR2(10 CHAR) NOT NULL
);

ALTER TABLE tiempos
    ADD CONSTRAINT tiempos_pk PRIMARY KEY ( vuelta,
                                            tramo_codigo,
                                            tramo_circuito_nombre,
                                            piloto_nombre );

CREATE TABLE tramo (
    codigo            INTEGER NOT NULL,
    diferencia_altura INTEGER,
    tipo_asfalto      VARCHAR2(10 CHAR),
    velocidad_media   NUMBER,
    circuito_nombre   VARCHAR2(10 CHAR) NOT NULL
);

ALTER TABLE tramo ADD CONSTRAINT tramo_pk PRIMARY KEY ( codigo,
                                                        circuito_nombre );

ALTER TABLE acto_piloto
    ADD CONSTRAINT acto_piloto_acto_publico_fk FOREIGN KEY ( acto_publico_fecha )
        REFERENCES acto_publico ( fecha );

ALTER TABLE acto_piloto
    ADD CONSTRAINT acto_piloto_piloto_fk FOREIGN KEY ( piloto_nombre )
        REFERENCES piloto ( nombre );

ALTER TABLE carrera
    ADD CONSTRAINT carrera_circuito_fk FOREIGN KEY ( circuito_nombre )
        REFERENCES circuito ( nombre );

ALTER TABLE carrera
    ADD CONSTRAINT carrera_piloto_fk FOREIGN KEY ( piloto_nombre )
        REFERENCES piloto ( nombre );

ALTER TABLE empleado
    ADD CONSTRAINT empleado_equipo_fk FOREIGN KEY ( equipo_nombre )
        REFERENCES equipo ( nombre );

ALTER TABLE empleado
    ADD CONSTRAINT empleado_equipo_fkv2 FOREIGN KEY ( equipo_nombre2 )
        REFERENCES equipo ( nombre );

ALTER TABLE empleado
    ADD CONSTRAINT empleado_equipo_fkv3 FOREIGN KEY ( equipo_nombre3 )
        REFERENCES equipo ( nombre );

ALTER TABLE empleado
    ADD CONSTRAINT empleado_equipo_fkv4 FOREIGN KEY ( equipo_nombre4 )
        REFERENCES equipo ( nombre );

ALTER TABLE equipo
    ADD CONSTRAINT equipo_empleado_fk FOREIGN KEY ( empleado_codigo )
        REFERENCES empleado ( codigo );

ALTER TABLE equipo
    ADD CONSTRAINT equipo_empleado_fkv2 FOREIGN KEY ( empleado_codigo2 )
        REFERENCES empleado ( codigo );

ALTER TABLE oficial
    ADD CONSTRAINT oficial_equipo_fk FOREIGN KEY ( nombre )
        REFERENCES equipo ( nombre );

ALTER TABLE piloto
    ADD CONSTRAINT piloto_equipo_fk FOREIGN KEY ( equipo_nombre )
        REFERENCES equipo ( nombre );

ALTER TABLE pilotov2
    ADD CONSTRAINT pilotov1_piloto_fk FOREIGN KEY ( piloto_nombre )
        REFERENCES piloto ( nombre );

ALTER TABLE pilotov2
    ADD CONSTRAINT pilotov1_piloto_fkv1 FOREIGN KEY ( piloto_nombre1 )
        REFERENCES piloto ( nombre );

ALTER TABLE tiempos
    ADD CONSTRAINT tiempos_piloto_fk FOREIGN KEY ( piloto_nombre )
        REFERENCES piloto ( nombre );

ALTER TABLE tiempos
    ADD CONSTRAINT tiempos_tramo_fk FOREIGN KEY ( tramo_codigo,
                                                  tramo_circuito_nombre )
        REFERENCES tramo ( codigo,
                           circuito_nombre );

ALTER TABLE tramo
    ADD CONSTRAINT tramo_circuito_fk FOREIGN KEY ( circuito_nombre )
        REFERENCES circuito ( nombre );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            11
-- CREATE INDEX                             4
-- ALTER TABLE                             32
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
