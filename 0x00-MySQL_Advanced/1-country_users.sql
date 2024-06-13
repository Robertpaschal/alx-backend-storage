-- This script creates a table named 'users' with the specified attributes
-- It ensures the table will not be created if it already exits

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country CHAR(2) NOT NULL DEFAULT 'US' CHECK (country IN ('US', 'CO', 'TN'))
);