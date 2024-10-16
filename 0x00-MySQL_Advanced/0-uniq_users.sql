-- Creates a table users
-- users table created with attributes defined
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
		id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
		email VARCHAR(255) NOT NULL UNIQUE,
		name VARCHAR(255) );
