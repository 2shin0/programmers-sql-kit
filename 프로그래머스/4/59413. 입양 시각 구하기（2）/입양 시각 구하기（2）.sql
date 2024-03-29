-- 코드를 입력하세요
WITH RECURSIVE TIME AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1 
    FROM TIME
    WHERE HOUR < 23
)

SELECT b.HOUR, COUNT(a.ANIMAL_ID) AS COUNT
FROM ANIMAL_OUTS a
RIGHT JOIN TIME b
ON HOUR(a.DATETIME) = b.HOUR
GROUP BY HOUR
ORDER BY HOUR;