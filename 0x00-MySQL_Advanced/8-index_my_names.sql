-- create index on name table using the first letter of name
CREATE INDEX idx_name_first ON names (name(1));
