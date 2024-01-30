-- SQLite
--Sukurkite duomenų bazę, kurioje saugosite informaciją apie studentų duomenis
--ir jų kursus. Kiekvienas studentas gali mokytis daugelyje kursų,
--ir kiekvienas kursas gali turėti daug studentų. 
--Sukurkite atitinkamas lentelės ir susiekite jas Many-to-Many ryšiu.

CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,

