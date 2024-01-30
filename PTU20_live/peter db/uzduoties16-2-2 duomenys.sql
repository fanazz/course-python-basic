-- SQLite
--Sukurkite lentelę "mokytojai" su šiais stulpeliais: 
--"id", "vardas", "pavarde", "specialybe" ir "patirtis_metais".
DROP table teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    subject VARCHAR(50),
    career_start INTEGER
);

--Įterpkite įrašus į sukurtą lentelę "mokytojai"

INSERT INTO teachers (first_name, last_name,
subject, career_start)
VALUES ('Petras', 'Petraitis', 'Matematika', 2013),
       ('Ona', 'Onaitė', 'Fizika', 2012),
       ('Marius', 'Marijus', 'Biologija', 2015),
       ('Rasa', 'Rasaitė', 'Anglų kalba', 2011),
       ('Aurimas', 'Aurimaitis', 'Lietuvių kalba', 2018),
       ('Gintarė', 'Gintarėlė', 'Istorija', 2020);

--Parodykite visus įrašus iš lentelės "mokytojai", kurių specialybė yra "Matematika".
SELECT * FROM teachers WHERE subject = 'Matematika'

--Raskite visus mokytojus, kurių stažas yra ilgesnis nei 8 bet trumpesnis nei 12 metų,
-- ir atvaizduokite tik jų vardą, pavardę bei specialybę.

SELECT first_name, last_name, subject FROM teachers
WHERE (2024 - career_start) > 8 AND (2024 - career_start) < 12;

--Pakeiskite mokytojos, vardu Rasa ir pavarde Rasaitė, pavardę į "Žolienė"

UPDATE teachers
SET last_name = 'Žolienė'
WHERE first_name = 'Rasa' AND last_name = 'Rasaitė';

--Ištrinkite iš lentelės "mokytojai" mokytoją, kurio ID yra 4.

DELETE FROM teachers WHERE id = 4;

SELECT * FROM teachers