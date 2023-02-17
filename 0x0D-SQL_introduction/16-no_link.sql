-- lists all records of the table except those qith no value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
