--
-- @lc app=leetcode id=178 lang=mysql
--
-- [178] Rank Scores
--

-- @lc code=start
# Write your MySQL query statement below
-- SELECT
--     s.Score,
--     (SELECT COUNT(DISTINCT Score) FROM Scores WHERE Score >= s.Score) as Rank
-- FROM Scores s
-- ORDER BY s.Score DESC

-- 10/10 cases passed (756 ms)
-- Your runtime beats 53.55 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)

-- 2. With Variable
SELECT
    Score,
    @rank := @rank + (@prev <> (@prev := Score)) Rank
FROM
    Scores,
    (SELECT @rank := 0, @prev := -1) init
ORDER BY Score DESC

-- 10/10 cases passed (271 ms)
-- Your runtime beats 96.58 % of mysql submissions
-- Your memory usage beats 100 % of mysql submissions (0B)
-- @lc code=end

