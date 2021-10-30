#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 -U mysiteuser mysite <<-EOSQL

    \c "mysite";

    DROP SEQUENCE IF EXISTS "public"."user_id_seq";
    CREATE SEQUENCE "public"."user_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9254775807
    START 1
    CACHE 1;
    ALTER SEQUENCE "public"."user_id_seq" OWNER TO "mysiteuser";

    DROP TABLE IF EXISTS "public"."puser";
    CREATE TABLE "public"."puser" (
      "id" int4 NOT NULL DEFAULT 1,
      "name" varchar(255) COLLATE "pg_catalog"."default",
      "phone" varchar(255) COLLATE "pg_catalog"."default"
    ) ;
    ALTER TABLE "public"."muser" OWNER TO "mysiteuser";


    BEGIN;
    INSERT INTO "public"."puser" VALUES (1, 'song', '18801254191');
    INSERT INTO "public"."puser" VALUES (100, 'song', '100');
    INSERT INTO "public"."puser" VALUES (101, 'name1', '16654321232');
    COMMIT;

    SELECT setval('"public"."user_id_seq"', 2, false);

    ALTER TABLE "public"."puser" ADD CONSTRAINT "Muser_pkey" PRIMARY KEY ("id");
EOSQL