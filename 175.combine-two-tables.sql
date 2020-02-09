--
-- @lc app=leetcode id=175 lang=mysql
--
-- [175] Combine Two Tables
--

-- @lc code=start
# Write your MySQL query statement below
select p.FirstName, p.LastName, a.City, a.State
from Person p left join Address a on p.PersonId = a.PersonId;

-- 7/7 cases passed (478 ms)
-- Your runtime beats 72.49 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
-- @lc code=end

