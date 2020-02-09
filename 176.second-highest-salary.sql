--
-- @lc app=leetcode id=176 lang=mysql
--
-- [176] Second Highest Salary
--

-- @lc code=start
# Write your MySQL query statement below
-- select (select distinct Salary
-- from Employee
-- order by Salary desc
-- limit 1 offset 1) as SecondHighestSalary;

-- 7/7 cases passed (296 ms)
-- Your runtime beats 72.84 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)

-- select (select distinct Salary
-- from Employee
-- order by Salary desc
-- limit 1, 1) as SecondHighestSalary;

-- 7/7 cases passed (152 ms)
-- Your runtime beats 95.03 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)

SELECT max(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee);

-- 7/7 cases passed (319 ms)
-- Your runtime beats 56.84 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
-- @lc code=end

