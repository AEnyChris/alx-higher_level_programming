-- display average temperature from temperature table

SELECT city, AVG(value) as avg_temp from temperature
GROUP BY city
ORDER BY avg_temp DESC;
