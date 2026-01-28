/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(nullptr) {}
 * };
 */

#include <vector>
#include <cstdlib>

using namespace std;

class Solution {
private:
    vector<int> values;

public:
    Solution(ListNode* head) {
        ListNode* current = head;
        while (current) {
            values.push_back(current->val);
            current = current->next;
        }
    }

    int getRandom() {
        int index = rand() % values.size();
        return values[index];
    }
};
