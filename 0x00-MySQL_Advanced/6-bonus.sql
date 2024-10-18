-- creates a stored procedure
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER //
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
		-- First create new project if project_name does not exist in projects table
		IF (SELECT name FROM projects WHERE name = project_name) IS NULL THEN
				INSERT INTO projects(name) VALUES(project_name);
		END IF;

		-- Insert the new correction into the corrections table
		INSERT INTO corrections(user_id, project_id, score)
			VALUES(user_id, (SELECT id FROM projects WHERE name = project_name), score);

END;//
DELIMITER ;
