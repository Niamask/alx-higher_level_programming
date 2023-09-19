-- lists all records of the table second_table of the database hbtn_0c_0;

DELETE FROM second_table WHERE 	name = 'George';
INSERT INTO second_table (id , name, score) VALUES (3, 'Aria', 18), (4, 'Aria', 12);
SELECT score, name FROM second_table ORDER BY score DESC;
