--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
--  1. Join
# Write your MySQL query statement below
-- select e.name Employee
--     from Employee e join Employee m on e.ManagerId = m.Id
--     where e.Salary > m.Salary;

-- 14/14 cases passed (459 ms)
-- Your runtime beats 86.71 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)

select e.name Employee
    from Employee e, Employee m
    where e.ManagerId = m.Id and e.Salary > m.Salary;

-- 14/14 cases passed (1373 ms)
-- Your runtime beats 5 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
-- @lc code=end

