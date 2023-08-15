-- display average temperatures grouped by city
-- quite needed to get and have
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC
