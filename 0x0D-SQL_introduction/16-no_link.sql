-- lists all records that have a name value
SELECT score, name FROM second_table WHERE name != '' AND name IS NOT NULL ORDER BY score DESC;
