-- Create stored procedure to calculate average score
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER ??
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
		DECLARE avg_score FLOAT DEFAULT 0.0;

		SELECT AVG(corrections.score)
		INTO avg_score
		FROM corrections
		WHERE corrections.user_id = user_id;

		UPDATE users SET users.average_score = avg_score
		WHERE users.id = user_id;
END;??
DELIMITER ;
