#
# @lc app=leetcode id=193 lang=bash
#
# [193] Valid Phone Numbers
#
# https://leetcode.com/problems/valid-phone-numbers/description/
#
# shell
# Easy (25.23%)
# Likes:    139
# Dislikes: 346
# Total Accepted:    33.6K
# Total Submissions: 132.9K
# Testcase Example:  '0'
#
# Given a text file file.txt that contains list of phone numbers (one per
# line), write a one liner bash script to print all valid phone numbers.
# 
# You may assume that a valid phone number must appear in one of the following
# two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
# 
# You may also assume each line in the text file must not contain leading or
# trailing white spaces.
# 
# Example:
# 
# Assume that file.txt has the following content:
# 
# 
# 987-123-4567
# 123 456 7890
# (123) 456-7890
# 
# 
# Your script should output the following valid phone numbers:
# 
# 
# 987-123-4567
# (123) 456-7890
# 
# 
#

# @lc code=start
# Read from the file file.txt and output all valid phone numbers to stdout.
# grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
# 26/26 cases passed (4 ms)
# Your runtime beats 57.26 % of bash submissions
# Your memory usage beats 39.29 % of bash submissions (3.2 MB)

# sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt
# 26/26 cases passed (4 ms)
# Your runtime beats 57.26 % of bash submissions
# Your memory usage beats 96.43 % of bash submissions (3.1 MB)

awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt
# 26/26 cases passed (4 ms)
# Your runtime beats 57.26 % of bash submissions
# Your memory usage beats 14.29 % of bash submissions (3.3 MB)

# @lc code=end

