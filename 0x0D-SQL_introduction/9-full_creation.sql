-- create second_table and add some records
-- add values into created table
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
-- add some records
INSERT INTO second_table
VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8)
