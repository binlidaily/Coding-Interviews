#
# @lc app=leetcode id=195 lang=bash
#
# [195] Tenth Line
#
# https://leetcode.com/problems/tenth-line/description/
#
# shell
# Easy (33.50%)
# Likes:    155
# Dislikes: 163
# Total Accepted:    48.8K
# Total Submissions: 146K
# Testcase Example:  'Line 1\\nLine 2\\nLine 3\\nLine 4\\nLine 5\\nLine 6\\nLine 7\\nLine 8\\nLine 9\\nLine 10'
#
# Given a text file file.txt, print just the 10th line of the file.
# 
# Example:
# 
# Assume that file.txt has the following content:
# 
# 
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# 
# 
# Your script should output the tenth line, which is:
# 
# 
# Line 10
# 
# 
# Note:
# 1. If the file contains less than 10 lines, what should you output?
# 2. There's at least three different solutions. Try to explore all
# possibilities.
# 
#

# @lc code=start
# Read from the file file.txt and output the tenth line to stdout.

# awk
# awk 'FNR == 10 {print }'  file.txt
# or
# awk 'NR==10' file.txt
# 7/7 cases passed (0 ms)
# Your runtime beats 100 % of bash submissions
# Your memory usage beats 85.71 % of bash submissions (3.7 MB)

# sed -n '10p' file.txt
# 7/7 cases passed (4 ms)
# Your runtime beats 73.92 % of bash submissions
# Your memory usage beats 100 % of bash submissions (3.6 MB)

# cnt=0
# while read line && [ $cnt -le 10 ]; do
#   let 'cnt = cnt + 1'
#   if [ $cnt -eq 10 ]; then
#     echo $line
#     exit 0
#   fi
# done < file.txt
# 7/7 cases passed (4 ms)
# Your runtime beats 73.92 % of bash submissions
# Your memory usage beats 100 % of bash submissions (3.6 MB)

tail -n+10 file.txt|head -1
# 7/7 cases passed (4 ms)
# Your runtime beats 73.92 % of bash submissions
# Your memory usage beats 52.38 % of bash submissions (3.7 MB)
# @lc code=end

