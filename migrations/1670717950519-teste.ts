import { MigrationInterface, QueryRunner } from 'typeorm';

export class teste1670717950519 implements MigrationInterface {
  name = 'teste1670717950519';

  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(
      `CREATE TABLE "usuario" ("id" uuid NOT NULL DEFAULT uuid_generate_v4(), "email" character varying(200) NOT NULL, "nome" character varying NOT NULL, "username" character varying NOT NULL, "cargo" character varying(200) NOT NULL, "perfil" character varying(20) NOT NULL, "password" character varying NOT NULL, "salt" character varying NOT NULL, "confirmationToken" character varying(64), "recoverToken" character varying(64), "createdAt" TIMESTAMP NOT NULL DEFAULT now(), "updatedAt" TIMESTAMP NOT NULL DEFAULT now(), CONSTRAINT "UQ_2863682842e688ca198eb25c124" UNIQUE ("email"), CONSTRAINT "PK_a56c58e5cabaa04fb2c98d2d7e2" PRIMARY KEY ("id"))`,
    );
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`DROP TABLE "usuario"`);
  }
}
