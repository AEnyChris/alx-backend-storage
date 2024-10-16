-- Creates a table users
-- users table created with attributes defined
DROP TABLE IF EXISTS;
CREATE TABLE IF NOT EXISTS users (
		id INT AUTO-INCREMENT NOT NULL PRIMARY KEY,
		email VARCHAR(255) NOT NULL UNIQUE,
		name VARCHAR(255) );
