#include <vector>
#include <unordered_map>
#include <cstdlib>

using namespace std;

class Solution {
private:
    unordered_map<int, vector<int>> numIndices;

public:
    Solution(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            numIndices[nums[i]].push_back(i);
        }
    }

    int pick(int target) {
        vector<int>& indices = numIndices[target];
        int randomIndex = rand() % indices.size();
        return indices[randomIndex];
    }
};
