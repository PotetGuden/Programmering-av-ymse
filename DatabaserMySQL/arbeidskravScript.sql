CREATE Schema arbeidskrav;



CREATE TABLE høyskolen_kristiania (
  person_id INT PRIMARY KEY,
  fornavn VARCHAR(40),
  etternavn VARCHAR(40),
  kjønn VARCHAR(1),
  super_id INT,
  fag_id INT 
);

CREATE TABLE fag (
  fag_id INT PRIMARY KEY,
  fag_navn VARCHAR(40),
  lærer_id INT,
  FOREIGN KEY(lærer_id) REFERENCES høyskolen_kristiania(person_id) ON DELETE SET NULL
);

ALTER TABLE høyskolen_kristiania
ADD FOREIGN KEY(fag_id)
REFERENCES fag(fag_id)
ON DELETE SET NULL;

ALTER TABLE høyskolen_kristiania
ADD FOREIGN KEY(super_id)
REFERENCES høyskolen_kristiania(person_id)
ON DELETE SET NULL;


-- Rektor
INSERT INTO høyskolen_kristiania VALUES(100, 'David', 'Gundersern', 'M', NULL, NULL);

INSERT INTO fag VALUES(1, 'Intro til Programmering', 100);

UPDATE høyskolen_kristiania
SET fag_id = 1
WHERE person_id = 100;


INSERT INTO høyskolen_kristiania VALUES(101, 'Knut', 'Knudsen', 'M', 100, 1);


-- Webprosjekt
INSERT INTO høyskolen_kristiania VALUES(102, 'Heidi', 'Gårdsrud', 'F', 100, NULL);

INSERT INTO fag VALUES(2, 'Webprosjekt', 102);

UPDATE høyskolen_kristiania
SET fag_id = 2
WHERE person_id = 102;

INSERT INTO høyskolen_kristiania VALUES(103, 'Angela', 'Lundgren', 'F', 102, 2);
INSERT INTO høyskolen_kristiania VALUES(104, 'Per', 'Pettersen', 'M', 102, 2);
INSERT INTO høyskolen_kristiania VALUES(105, 'Asgeir', 'Tomte', 'M', 102, 2);

-- Databaser
INSERT INTO høyskolen_kristiania VALUES(106, 'Thomas', 'Andnes', 'M', 100, NULL);

INSERT INTO fag VALUES(3, 'Databaser', 106);

UPDATE høyskolen_kristiania
SET fag_id = 3
WHERE person_id = 106;

INSERT INTO høyskolen_kristiania VALUES(107, 'Andreas', 'Andersen', 'M', 106, 3);
INSERT INTO høyskolen_kristiania VALUES(108, 'Tim', 'Bjergseth', 'M', 106, 3);

SELECT * FROM høyskolen_kristiania;
SELECT * FROM fag;


SELECT høyskolen_kristiania.person_id, høyskolen_kristiania.fornavn, fag.fag_navn
FROM høyskolen_kristiania
INNER JOIN fag
ON høyskolen_kristiania.person_id = fag.lærer_id;