use createtables;


DROP TABLE student; 

#constraints
#kan bruke AUTO_INCREMENT,NOT NULL,UNIQUE og DEFAULT(for å sette inn noe, hvis ikke brukeren gjør det), UNIQUE sier at det ikke kan være fler som har samme "felt"/"navn på kolonne"  - major VARCHAR(255) UNIQUE
#kan også bruke ENUM, "Continent ENUM ("Asia", "Europa", etc) NOT NULL"  ENUM vil da si at et land feks ikke kan ha fler av denne verdien, men man må velge mellom en av de.
#kan også definere en kolonne som primary key senere i CREATE TABLE ved å skrive på ny linje: PRIMARY KEY (student_id)
CREATE TABLE student(
	student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(35) NOT NULL,
    major VARCHAR(35) DEFAULT "undecided"
);

DESC student;

ALTER TABLE student 
ADD gpa DECIMAL(3,2);


ALTER TABLE student
DROP COLUMN gpa;

SELECT *
FROM student;

#siden jeg har auto_increment for id, men man må bruke (kolonne, kolonne)
INSERT INTO student (name,major) VALUES("Jack", "Biology");

INSERT INTO student VALUES(1, "Jack", "Biology");
INSERT INTO student VALUES(2, "Kate", "Sosiology");
INSERT INTO student VALUES(3, "Claire", "Chemistry");
INSERT INTO student VALUES(4, "Jack", "Biology");
INSERT INTO student VALUES(5, "Mike", "Computer Science");

#Denne kan man bruke hvis man bare vil endre/legge til info til noen kolonner
INSERT INTO student(student_id,name) VALUES(1, "Jack");

#For å endre en verdi i en kolonne feks.
UPDATE student
SET major = "Bio"
WHERE major = "Biology";

UPDATE student
SET major = "Comp Sci"
WHERE major = "Computer Science";
#kan endre feks PRIMARY KEY nummer 3 ved å skrive WHERE student_id = 3;

UPDATE student
SET major = "Biochemistry"
WHERE major = "Bio" OR major = "Chemistry";
#hvis man vil endre fler kolonne verdier samtidig

UPDATE student
SET name = "Tom", major = "undecided"
WHERE student_id = 1;
#hvis man vil endre 2 verdier for en annen verdi 

#eller hvis man vil endre alt i et
UPDATE student
SET major = "blankt";


#slette alle verdier i en tabell
DELETE FROM student;

#syntax for å slette en rad
DELETE FROM student
WHERE student_id = 5;

DELETE FROM student
WHERE name = "Tom" AND major = "blankt";




