# Write your MySQL query sta
update salary
set sex = case 
when sex = 'm' then 'f'
else 'm'
end;