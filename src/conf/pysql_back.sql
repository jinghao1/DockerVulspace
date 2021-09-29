/*
 Navicat Premium Data Transfer

 Source Server         : pysql
 Source Server Type    : PostgreSQL
 Source Server Version : 130004
 Source Host           : localhost:5432
 Source Catalog        : mysite
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 130004
 File Encoding         : 65001

 Date: 26/09/2021 16:19:30
*/


-- ----------------------------
-- Sequence structure for user_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."user_id_seq";
CREATE SEQUENCE "public"."user_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "public"."user_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Table structure for muser
-- ----------------------------
DROP TABLE IF EXISTS "public"."muser";
CREATE TABLE "public"."muser" (
  "id" int4 NOT NULL DEFAULT 1,
  "name" varchar(255) COLLATE "pg_catalog"."default",
  "phone" varchar(255) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "public"."muser" OWNER TO "postgres";

-- ----------------------------
-- Records of muser
-- ----------------------------
BEGIN;
INSERT INTO "public"."muser" VALUES (1, 'song', '18801254191');
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "public"."user";
CREATE TABLE "public"."user" (
  "id" int4 NOT NULL DEFAULT 1,
  "name" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "phone" varchar(20) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying
)
;
ALTER TABLE "public"."user" OWNER TO "wangm";

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO "public"."user" VALUES (1, 'song', '15512727702');
COMMIT;

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."user_id_seq"', 2, false);

-- ----------------------------
-- Primary Key structure for table muser
-- ----------------------------
ALTER TABLE "public"."muser" ADD CONSTRAINT "Muser_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table user
-- ----------------------------
ALTER TABLE "public"."user" ADD CONSTRAINT "user_pkey" PRIMARY KEY ("id");
