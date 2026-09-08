# Write your MySQL query statement below
select d.name as Department,e.name as Employee,e.salary as Salary 
from Employee e
join Department d
on e.departmentId=d.Id
join(
    select departmentId,max(salary) as MAX_salary
    from employee
    group by departmentId
)m
on e.departmentId=m.departmentId
AND e.salary=m.MAX_salary;