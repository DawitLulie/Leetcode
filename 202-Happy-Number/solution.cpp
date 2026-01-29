#include <unordered_set>

using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> seen;

        while (n != 1 && seen.find(n) == seen.end()) {
            seen.insert(n);
            n = getNextNumber(n);
        }

        return n == 1;
    }

private:
    int getNextNumber(int number) {
        int sum = 0;
        while (number > 0) {
            int digit = number % 10;
            sum += digit * digit;
            number /= 10;
        }
        return sum;
    }
};
