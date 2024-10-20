-- create a procedure to calculate weighted average
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
		DECLARE score_by_weight INT DEFAULT 0;
		DECLARE weight_sum INT DEFAULT 0;

		SELECT SUM(corrections.score * projects.weight) INTO score_by_weight
	   	FROM corrections
		JOIN projects ON corrections.project_id = projects.id
		WHERE corrections.user_id = user_id;

		SELECT SUM(weight) INTO weight_sum FROM projects;

		UPDATE users SET average_score = score_by_weight / weight_sum
		WHERE users.id = user_id;
END;//
DELIMITER ;
