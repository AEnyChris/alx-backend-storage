-- create a trigger to update items on change in order
DELIMITER ##
CREATE TRIGGER update_items 
AFTER INSERT ON orders
FOR EACH ROW
		BEGIN
				UPDATE items
				SET quantity = quantity - NEW.number
				WHERE name = NEW.item_name;
		END;##
DELIMITER ; 
