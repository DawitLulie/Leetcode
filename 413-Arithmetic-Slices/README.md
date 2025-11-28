<h2><a href="https://leetcode.com/problems/arithmetic-slices">413. Arithmetic Slices</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.</p>

<p>For example, <code>[1,3,5,7,9]</code> is arithmetic because the differences between consecutive elements are all <code>2</code>.</p>

<p>Given an integer array <code>nums</code>, return the number of arithmetic subarrays of <code>nums</code>.</p>

<p>A subarray is a contiguous subsequence of the array.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,3,4]
Output: 3
Explanation: The arithmetic slices are:
[1,2,3], [2,3,4] and [1,2,3,4]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1]
Output: 0
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 &lt;= nums.length &lt;= 5000</li>
  <li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

---

### Solution

**Approach:**  
Use dynamic counting.  
If the current difference equals the previous difference, increase the current streak.  
Each time a streak extends, it adds new arithmetic slices.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---
