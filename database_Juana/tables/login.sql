CREATE DATABASE IF NOT EXISTS juana_login;
USE juana_login;
CREATE TABLE IF NOT EXISTS user(
    id SMALLINT(3) AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20),
    password CHAR(102),
    fullname VARCHAR(50)
);
