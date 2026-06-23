# Write your MySQL query state
SELECT firstName, lastName, city, state from Person
left join Address ON Person.PersonId=Address.personId;