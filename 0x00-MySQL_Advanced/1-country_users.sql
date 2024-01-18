-- SQL script that creates a table
-- if table already exists, script should not fail
-- script can be executed on any database
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar (255)
	country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
	);
