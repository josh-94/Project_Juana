CREATE DATABASE IF NOT EXISTS BD_juana;
USE BD_juana;
CREATE TABLE IF NOT EXISTS user(
    id SMALLINT(3) AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20),
    password CHAR(102),
    fullname VARCHAR(50)
);