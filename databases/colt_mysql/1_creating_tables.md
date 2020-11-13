# Creating tables

## Data types

Numeric - INT
Text - VARCHAR

Varchar between 1 to 255 characters.

    CREATE TABLE tablename
    (
        column_name data_type,
        column_name data_type
    );

    CREATE TABLE cats
    (
        name VARCHAR(100),
        age INT
    );

    CREATE TABLE posts
    (
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        slug VARCHAR(100),
        body TEXT
    );

## Show tables

    show tables;

    show columns from tablename;