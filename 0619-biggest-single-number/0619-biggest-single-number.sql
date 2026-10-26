SELECT MAX(num) AS num
FROM mynumbers
WHERE num NOT IN (
    SELECT num
    FROM mynumbers
    GROUP BY num
    HAVING COUNT(*) > 1
);