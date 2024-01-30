-- SQLite
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    program VARCHAR(100),
    email VARCHAR(50)
);

ALTER TABLE students ADD birth_date DATE;
DROP TABLE students;