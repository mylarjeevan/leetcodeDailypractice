# Write your MySQL query statement below
select name from salesperson 
where sales_id not in (
SELECT DISTINCT s.sales_id
FROM orders o
LEFT JOIN company c
    ON o.com_id = c.com_id
LEFT JOIN salesperson s
    ON s.sales_id = o.sales_id
WHERE c.name = 'RED');;