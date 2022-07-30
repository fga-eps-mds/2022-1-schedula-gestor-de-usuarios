CREATE DATABASE gestor_de_usuarios;

\c gestor_de_usuarios

CREATE SCHEMA IF NOT EXISTS "public";

CREATE TYPE "public"."acess" AS ENUM ('admin', 'basic', 'manager');

CREATE TABLE "public"."user" (
    username      VARCHAR(250)         NOT NULL,
    name    VARCHAR(250)    NOT NULL,
    job_role    VARCHAR(250)    NOT NULL,
    email    VARCHAR(100)    NOT NULL,
    password    TEXT    NOT NULL,
    active    BOOLEAN         NOT NULL DEFAULT TRUE,
    updated_at    TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    acess  "public"."acess"    NOT NULL DEFAULT 'basic',

    CONSTRAINT "PK_username" PRIMARY KEY ( "username" )   
);