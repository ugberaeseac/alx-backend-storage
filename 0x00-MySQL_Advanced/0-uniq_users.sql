- SQL script that creates a table
- if table already exists, script should not fail
- script can be executed on any database
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO INCREMENT,
	email varchar(256) NOT NULL UNIQUE,
	name varchar (256)
	);
