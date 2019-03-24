-- MYSQL

CREATE DATABASE IF NOT EXISTS similar_importers;

use similar_importers;

DROP TABLE IF EXISTS `importers_products`;
DROP TABLE IF EXISTS `distances`;
DROP TABLE IF EXISTS `importers`;
DROP TABLE IF EXISTS `products`;

CREATE TABLE `importers` (
	`importer_id` INT NOT NULL,
	`importer_name` TEXT NOT NULL,
	PRIMARY KEY (`importer_id`)
);

CREATE TABLE `products` (
	`product_id` INT NOT NULL,
	`product_name` TEXT NOT NULL,
	PRIMARY KEY (`product_id`)
);

CREATE TABLE `importers_products` (
	`importer_id` INT NOT NULL,
	`product_id` INT NOT NULL,
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
