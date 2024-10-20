-- create a procedure to calculate weighted average
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
		ALTER TABLE users ADD score_by_weight INT NOT NULL;
		ALTER TABLE users ADD weight_sum INT NOT NULL;

		UPDATE users
		SET score_by_weight = (
				SELECT SUM(corrections.score * projects.weight)
				FROM corrections
				INNER JOIN projects ON corrections.project_id = projects.id
				WHERE corrections.user_id = users.id
		);

		UPDATE users
			SET weight_sum = (
				SELECT SUM(projects.weight)
				FROM corrections
				JOIN projects ON corrections.project_id = projects.id
				WHERE corrections.user_id - users.id
		);

		UPDATE users
		SET users.average_score = IF(users.weight_sum = 0, 0, users.score_by_weight / users.weight_sum);

		ALTER TABLE users DROP column score_by_weight;
		ALTER TABLE users DROP column weight_sum;
END //
DELIMITER ;
