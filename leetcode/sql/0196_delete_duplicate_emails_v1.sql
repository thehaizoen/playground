-- 196. Delete Duplicate Emails (Answer v1)
-- Problem Link: https://leetcode.com/problems/delete-duplicate-emails/
-- Solution Link (Personal): 

DELETE p1
FROM Person p1
JOIN Person p2 
ON p1.email = p2.email
WHERE p1.id > p2.id;
