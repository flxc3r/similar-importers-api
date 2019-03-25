-- MYSQL

CREATE DATABASE IF NOT EXISTS similar_importers;

use similar_importers;

DROP TABLE IF EXISTS `importers_products`;
DROP TABLE IF EXISTS `importers_addresses`;
DROP TABLE IF EXISTS `distances`;
DROP TABLE IF EXISTS `importers`;
DROP TABLE IF EXISTS `products`;

CREATE TABLE `importers` (
	`importer_id` INT NOT NULL,
	`importer_name` TEXT NOT NULL,
	PRIMARY KEY (`importer_id`)
);

CREATE TABLE `importers_addresses` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`importer_id` INT NOT NULL,
	`city` TEXT,
	`province` TEXT,
	`postalcode` TEXT,
	PRIMARY KEY (`id`),
	FOREIGN KEY (importer_id) REFERENCES importers(importer_id)
);

CREATE TABLE `products` (
	`product_id` VARCHAR(10) NOT NULL,
	`product_name` TEXT NOT NULL,
	PRIMARY KEY (`product_id`)
);

CREATE TABLE `importers_products` (
	`importer_id` INT NOT NULL,
	`product_id` VARCHAR(10) NOT NULL,
	PRIMARY KEY (`importer_id`,`product_id`),
    FOREIGN KEY (importer_id) REFERENCES importers(importer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE `distances` (
	`importer_id` INT NOT NULL,
	`similar_importer_id` INT NOT NULL,
	`distance` FLOAT NOT NULL,
	PRIMARY KEY (`importer_id`,`similar_importer_id`),
    FOREIGN KEY (importer_id) REFERENCES importers(importer_id),
    FOREIGN KEY (similar_importer_id) REFERENCES importers(importer_id)
);
