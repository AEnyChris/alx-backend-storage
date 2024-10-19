-- create view from students table
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS SELECT name FROM students 
WHERE students.score < 80
AND (last_meeting IS NULL OR last_meeting < SUBDATE(CURRENT_DATE(), INTERVAL 1 MONTH));
