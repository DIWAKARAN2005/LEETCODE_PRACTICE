# Write your MySQL query statement below
select e.name,b.bonus from Employee e Left join bonus b on e.empid = b.empid Where b.bonus < 1000 or b.bonus is null;