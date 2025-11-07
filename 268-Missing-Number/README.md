<h2><a href="https://leetcode.com/problems/missing-number">Missing Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an array <code>nums</code> containing <code>n</code> distinct numbers in the range <code>[0, n]</code>, return the only number in the range that is missing from the array.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3, so the numbers are in the range [0,3]. 2 is missing.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [0,1]
Output: 2
Explanation: n = 2, numbers are [0,2], 2 is missing.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>n == nums.length</li>
  <li>1 &lt;= n &lt;= 10<sup>4</sup></li>
  <li>0 &lt;= nums[i] &lt;= n</li>
  <li>All the numbers of <code>nums</code> are unique.</li>
</ul>

---

### Solution

**Approach:**  
Use the formula for the sum of first n natural numbers.  
Subtract the sum of the array from the expected total to find the missing number.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---
