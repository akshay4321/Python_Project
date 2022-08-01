BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Login" (
	"Uid"	INTEGER,
	"Uname"	VARCHAR(100) NOT NULL,
	"Password"	VARCHAR(50) NOT NULL,
	"access_count"	INTEGER DEFAULT 0,
	PRIMARY KEY("Uid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Location" (
	"location_id"	INTEGER NOT NULL,
	"location_name"	VARCHAR(100) NOT NULL,
	"province"	VARCHAR(100) NOT NULL,
	"country"	VARCHAR(100) NOT NULL,
	"postal_code"	VARCHAR(50) NOT NULL,
	"createdate_time"	DATETIME NOT NULL,
	"update_datetime"	DATETIME NOT NULL,
	"delete_status"	INTEGER NOT NULL,
	PRIMARY KEY("location_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Hotel" (
	"hotel_id"	INTEGER NOT NULL,
	"location_id"	INTEGER NOT NULL,
	"hotel_name"	VARCHAR(100) NOT NULL,
	"description"	VARCHAR(255) NOT NULL,
	"price"	float NOT NULL,
	"total_number_rooms"	INTEGER NOT NULL,
	"createdate_time"	DATETIME NOT NULL,
	"update_datetime"	DATETIME NOT NULL,
	"delete_status"	INTEGER NOT NULL,
	CONSTRAINT "FK_LocationHotel" FOREIGN KEY("location_id") REFERENCES "Location"("location_id"),
	PRIMARY KEY("hotel_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Package" (
	"package_id"	INTEGER NOT NULL,
	"location_id"	INTEGER NOT NULL,
	"package_name"	VARCHAR(100) NOT NULL,
	"description"	VARCHAR(255) NOT NULL,
	"price"	float NOT NULL,
	"total_number_package"	INTEGER NOT NULL,
	"package_type"	VARCHAR(100) NOT NULL,
	"createdate_time"	DATETIME NOT NULL,
	"update_datetime"	DATETIME NOT NULL,
	"delete_status"	INTEGER NOT NULL,
	CONSTRAINT "FK_LocationHotel" FOREIGN KEY("location_id") REFERENCES "Location"("location_id"),
	PRIMARY KEY("package_id" AUTOINCREMENT)
);
INSERT INTO "Location" ("location_id","location_name","province","country","postal_code","createdate_time","update_datetime","delete_status") VALUES (1,'waterloo','on','canada','n2j2c6','2022-07-24 16:19:40.444346','2022-07-24 17:07:31.294870',0),
 (2,'kitchener','on','canada','n2k2y9','2022-07-24 16:21:07.527204','2022-07-24 17:16:53.936623',1),
 (3,'cambridge','on','canada','w2e2e3','2022-07-24 17:16:09.982876','2022-07-24 17:16:45.963252',0);
INSERT INTO "Package" ("package_id","location_id","package_name","description","price","total_number_package","package_type","createdate_time","update_datetime","delete_status") VALUES (1,1,'city tour','Includes all unquie places of city',500.0,1,'city tour','2022-07-25 18:19:54.158866','2022-07-25 18:19:54.158866',0);
COMMIT;
