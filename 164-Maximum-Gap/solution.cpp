#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumGap(std::vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;

        std::sort(nums.begin(), nums.end());

        int maxGap = 0;
        for (int i = 1; i < n; i++) {
            maxGap = std::max(maxGap, nums[i] - nums[i - 1]);
        }

        return maxGap;
    }
};

