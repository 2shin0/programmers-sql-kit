SELECT F.ID, I.FISH_NAME, F.LENGTH
FROM FISH_INFO F
JOIN FISH_NAME_INFO I USING(FISH_TYPE)
WHERE (F.FISH_TYPE, F.LENGTH) IN (
    SELECT FISH_TYPE, MAX(LENGTH) 
    FROM FISH_INFO 
    GROUP BY FISH_TYPE
)
ORDER BY F.ID;
