-- list all recode in the table second_table with a score>10
-- recode are ordered by descending score
SELECT 'score', 'name'
FROM 'second_table'
WHERE 'score' >= 10
ORDER BY 'score' DESC;
