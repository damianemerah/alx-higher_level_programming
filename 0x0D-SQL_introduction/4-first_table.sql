-- create table 'first_table' in the current database
-- does not fail
CREATE TABLE IF NOT EXISTS first_table (id INT, 
	name VARCHAR(256));
