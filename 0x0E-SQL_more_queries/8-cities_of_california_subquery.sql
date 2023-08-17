-- select all cities in california by getting id from second table
-- where name is Cali
SELECT id, name FROM cities WHERE state_id=(SELECT id FROM states
WHERE name="California") ORDER BY id
