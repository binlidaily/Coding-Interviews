--
-- @lc app=leetcode id=177 lang=mysql
--
-- [177] Nth Highest Salary
--

-- @lc code=start
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT DEFAULT N-1;
-- DECLARE M INT;
-- SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT ( SELECT DISTINCT Salary
      FROM Employee
      ORDER by Salary DESC
      -- LIMIT 1 offset M
      LIMIT M, 1
      )
  );
END

-- 14/14 cases passed (184 ms)
-- Your runtime beats 97.82 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
-- @lc code=end

