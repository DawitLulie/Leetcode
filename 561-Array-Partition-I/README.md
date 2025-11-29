<h2><a href="https://leetcode.com/problems/array-partition-i">Array Partition I</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code> of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring order) are:
1. (1,4),(2,3) -> min(1,4)+min(2,3)=1+2=3
2. (1,3),(2,4) -> min(1,3)+min(2,4)=1+2=3
3. (1,2),(3,4) -> min(1,2)+min(3,4)=1+3=4
The maximum sum is 4.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [6,2,6,5,1,2]
Output: 9
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>nums.length == 2 * n</li>
  <li>1 &lt;= n &lt;= 10<sup>4</sup></li>
  <li>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></li>
</ul>

---

### Solution

**Approach:**  
Sort the array. Pair numbers consecutively.  
The sum of the smaller number in each pair is maximized by picking every first element in the sorted array.

**Complexity:**  
- Time: **O(n log n)** (due to sorting)  
- Space: **O(1)**

---
