-- get top 3 max temperature and the state they were in
-- because it's necessary
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state
ORDER BY state LIMIT 3
