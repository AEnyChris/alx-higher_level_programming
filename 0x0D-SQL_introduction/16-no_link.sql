-- lists all records of the table second_table of the database hbtn_0c_0
-- rows without a name value should not be displayed

SELECT score, name FROM second_table
WHERE name IS NOT NULL
AND name != ''
ORDER BY score DESC;
