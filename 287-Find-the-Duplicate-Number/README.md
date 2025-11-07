<h2><a href="https://leetcode.com/problems/find-the-duplicate-number">Find the Duplicate Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an array of integers <code>nums</code> containing <code>n + 1</code> integers where each integer is in the range <code>[1, n]</code> inclusive, there is only **one repeated number** in <code>nums</code>. Return this repeated number.</p>

<p>You must solve the problem **without modifying the array** <code>nums</code> and uses only constant extra space.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,3,4,2,2]
Output: 2
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [3,1,3,4,2]
Output: 3
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>2 &lt;= n &lt;= 10<sup>5</sup></li>
  <li>nums.length == n + 1</li>
  <li>1 &lt;= nums[i] &lt;= n</li>
  <li>All the integers in <code>nums</code> appear only once except for **one integer** which appears **two or more times**.</li>
</ul>

---

### Solution

**Approach:**  
Use Floyd's Tortoise and Hare (cycle detection) algorithm.  
Treat the array as a linked list and find the cycle entrance, which is the duplicate number.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---
