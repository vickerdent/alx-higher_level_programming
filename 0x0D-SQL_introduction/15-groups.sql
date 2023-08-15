-- return count of each score
-- then group by score, while ordering
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score ORDER BY COUNT(score) DESC
