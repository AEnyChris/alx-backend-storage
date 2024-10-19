-- create a function to return (a/b)
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
RETURN IF(b = 0, 0, (a / b));