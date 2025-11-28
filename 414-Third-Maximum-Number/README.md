<h2><a href="https://leetcode.com/problems/third-maximum-number">414. Third Maximum Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code>, return the <strong>third distinct maximum number</strong> in this array. If the third distinct maximum does not exist, return the <strong>maximum number</strong>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [3,2,1]
Output: 1
Explanation: The third distinct maximum is 1.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,2]
Output: 2
Explanation: The third distinct maximum does not exist, so return the maximum (2).
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [2,2,3,1]
Output: 1
Explanation: The third distinct maximum is 1.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
  <li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

---

### Solution

**Approach:**  
Track the top 3 distinct maximums using variables.  
Iterate through all numbers and update the top 3 accordingly.  
If the third maximum does not exist, return the highest maximum.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---
