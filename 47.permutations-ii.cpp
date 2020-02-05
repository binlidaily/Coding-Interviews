/*
 * @lc app=leetcode id=47 lang=cpp
 *
 * [47] Permutations II
 */
#include <iostream>
#include <vector>
using namespace std;
// @lc code=start
// Time: O(n!)
// Space: O(n)
class Solution {
public:
    vector<vector<int> > permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> path;
        vector<vector<int> > res;
        dfs(nums, path, res);
        return res;
    }
    void dfs(vector<int>& nums, vector<int> path, vector<vector<int> >& res){
        if (nums.empty() || nums.size() == 0){
            res.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); i++){
            if(i > 0 && nums[i-1] == nums[i]){
                continue;
            }
            path.push_back(nums[i]);
            vector<int> tmp = nums;
            tmp.erase(tmp.begin()+i);
            dfs(tmp, path, res);
            path.pop_back();
        }
    }
};
// 30/30 cases passed (28 ms)
// Your runtime beats 43.33 % of cpp submissions
// Your memory usage beats 14.28 % of cpp submissions (11.9 MB)
// @lc code=end

void print(vector<vector<int> > const &input)
{
    for (int i = 0; i < input.size(); i++) {
        for (int j = 0; j < input[i].size(); j++){
            cout << input[i][j] << ' ';
        }
        cout << endl;
    }
}
int main(){
    Solution* sol = new Solution();
    vector<int> test = {1, 1, 2};
    vector<vector<int> > res = sol->permuteUnique(test);
    print(res);
}
