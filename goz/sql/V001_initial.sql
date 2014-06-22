BEGIN;
CREATE TABLE "dbapi_user_friends" (
    "id" serial NOT NULL PRIMARY KEY,
    "from_user_id" integer NOT NULL,
    "to_user_id" integer NOT NULL,
    UNIQUE ("from_user_id", "to_user_id")
)
;
CREATE TABLE "dbapi_user" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "username" varchar(255) NOT NULL UNIQUE,
    "password" varchar(255) NOT NULL,
    "first_name" varchar(255) NOT NULL,
    "last_name" varchar(255) NOT NULL,
    "gender" varchar(2) NOT NULL,
    "birth_date" date,
    "photo" varchar(255) NOT NULL,
    "city" varchar(255) NOT NULL,
    "bio" text NOT NULL,
    "email" varchar(75) NOT NULL,
    "facebook" varchar(255) NOT NULL,
    "twitter" varchar(255) NOT NULL,
    "creation_date" timestamp with time zone NOT NULL,
    "last_update" timestamp with time zone NOT NULL
)
;
ALTER TABLE "dbapi_user_friends" ADD CONSTRAINT "from_user_id_refs_id_17f992f7" FOREIGN KEY ("from_user_id") REFERENCES "dbapi_user" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "dbapi_user_friends" ADD CONSTRAINT "to_user_id_refs_id_17f992f7" FOREIGN KEY ("to_user_id") REFERENCES "dbapi_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE TABLE "dbapi_categorie" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(255) NOT NULL,
    "icon" varchar(255) NOT NULL,
    "creation_date" timestamp with time zone NOT NULL,
    "last_update" timestamp with time zone NOT NULL,
    "active" boolean NOT NULL
)
;
CREATE TABLE "dbapi_zone" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(255) NOT NULL,
    "king_id" integer NOT NULL REFERENCES "dbapi_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "stroke_colour" varchar(7) NOT NULL,
    "stroke_weight" varchar(1) NOT NULL,
    "stroke_opacity" varchar(1) NOT NULL,
    "fill_colour" varchar(7) NOT NULL,
    "fill_opacity" varchar(3) NOT NULL,
    "points" text NOT NULL,
    "creation_date" timestamp with time zone NOT NULL,
    "last_update" timestamp with time zone NOT NULL,
    "active" boolean NOT NULL
)
;
CREATE TABLE "dbapi_venue" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(255) NOT NULL,
    "lat" varchar(255) NOT NULL,
    "lng" varchar(255) NOT NULL,
    "foursquare_url" varchar(50) NOT NULL,
    "categorie_id" integer NOT NULL REFERENCES "dbapi_categorie" ("id") DEFERRABLE INITIALLY DEFERRED,
    "zone_id" integer NOT NULL REFERENCES "dbapi_zone" ("id") DEFERRABLE INITIALLY DEFERRED,
    "creation_date" timestamp with time zone NOT NULL,
    "last_update" timestamp with time zone NOT NULL,
    "active" boolean NOT NULL
)
;
CREATE TABLE "dbapi_item" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(255) NOT NULL,
    "description" varchar(255) NOT NULL,
    "attack" smallint NOT NULL,
    "defense" smallint NOT NULL,
    "speed" smallint NOT NULL,
    "reach" smallint CHECK ("reach" >= 0) NOT NULL,
    "price" smallint CHECK ("price" >= 0) NOT NULL,
    "duration" smallint CHECK ("duration" >= 0) NOT NULL,
    "icon" varchar(255) NOT NULL,
    "creation_date" timestamp with time zone NOT NULL,
    "last_update" timestamp with time zone NOT NULL,
    "active" boolean NOT NULL
)
;
CREATE TABLE "dbapi_badge" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(255) NOT NULL,
    "description" varchar(255) NOT NULL,
    "unlock_message" varchar(255) NOT NULL,
    "level" smallint CHECK ("level" >= 0) NOT NULL,
    "icon" varchar(255) NOT NULL,
    "creation_date" timestamp with time zone NOT NULL,
    "last_update" timestamp with time zone NOT NULL,
    "active" boolean NOT NULL
)
;
CREATE TABLE "dbapi_score" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "dbapi_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "zone_id" integer NOT NULL REFERENCES "dbapi_zone" ("id") DEFERRABLE INITIALLY DEFERRED,
    "points" integer CHECK ("points" >= 0) NOT NULL,
    "creation_date" timestamp with time zone NOT NULL,
    "last_update" timestamp with time zone NOT NULL,
    UNIQUE ("user_id", "zone_id")
)
;
CREATE TABLE "dbapi_checkin" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "dbapi_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "venue_id" integer NOT NULL REFERENCES "dbapi_venue" ("id") DEFERRABLE INITIALLY DEFERRED,
    "number" integer CHECK ("number" >= 0) NOT NULL,
    "process" boolean NOT NULL,
    "creation_date" timestamp with time zone NOT NULL,
    "last_update" timestamp with time zone NOT NULL,
    UNIQUE ("user_id", "venue_id")
)
;
CREATE TABLE "dbapi_purchase" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "dbapi_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "item_id" integer NOT NULL REFERENCES "dbapi_item" ("id") DEFERRABLE INITIALLY DEFERRED,
    "number" integer CHECK ("number" >= 0) NOT NULL,
    "creation_date" timestamp with time zone NOT NULL,
    "last_update" timestamp with time zone NOT NULL,
    UNIQUE ("user_id", "item_id")
)
;
CREATE TABLE "dbapi_unlocking" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "dbapi_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "badge_id" integer NOT NULL REFERENCES "dbapi_badge" ("id") DEFERRABLE INITIALLY DEFERRED,
    "creation_date" timestamp with time zone NOT NULL,
    "last_update" timestamp with time zone NOT NULL,
    UNIQUE ("user_id", "badge_id")
)
;
CREATE TABLE "dbapi_event" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(255) NOT NULL,
    "description" varchar(255) NOT NULL,
    "start_date" date NOT NULL,
    "end_date" date NOT NULL,
    "status" varchar(3) NOT NULL,
    "venues_id" integer NOT NULL REFERENCES "dbapi_venue" ("id") DEFERRABLE INITIALLY DEFERRED,
    "zones_id" integer NOT NULL REFERENCES "dbapi_zone" ("id") DEFERRABLE INITIALLY DEFERRED,
    "items_id" integer NOT NULL REFERENCES "dbapi_item" ("id") DEFERRABLE INITIALLY DEFERRED,
    "categories_id" integer NOT NULL REFERENCES "dbapi_categorie" ("id") DEFERRABLE INITIALLY DEFERRED,
    "users_id" integer NOT NULL REFERENCES "dbapi_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "creation_date" timestamp with time zone NOT NULL,
    "last_update" timestamp with time zone NOT NULL,
    "active" boolean NOT NULL
)
;

COMMIT;
