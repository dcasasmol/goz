BEGIN;
ALTER TABLE "dbapi_item" ADD COLUMN "active" boolean NOT NULL;
ALTER TABLE "dbapi_badge" ADD COLUMN "active" boolean NOT NULL;
ALTER TABLE "dbapi_event" ADD COLUMN "active" boolean NOT NULL;
ALTER TABLE "dbapi_categorie" ADD COLUMN "active" boolean NOT NULL;
ALTER TABLE "dbapi_zone" ADD COLUMN "active" boolean NOT NULL;

COMMIT;
