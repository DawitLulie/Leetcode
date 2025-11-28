<h2><a href="https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array">448. Find All Numbers Disappeared in an Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an array <code>nums</code> of <code>n</code> integers where <code>nums[i]</code> is in the range <code>[1, n]</code>, return an array of all the integers in the range <code>[1, n]</code> that do not appear in <code>nums</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,1]
Output: [2]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>n == nums.length</code></li>
  <li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
  <li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>

---

### Solution

**Approach:**  
Use the input array itself to mark visited numbers.  
For each value <code>x</code> in <code>nums</code>, mark index <code>x - 1</code> as negative.  
After marking, the indices that remain positive are the missing numbers.

**Complexity:**  
- Time: O(n)  
- Space: O(1) (ignoring output array)

---
