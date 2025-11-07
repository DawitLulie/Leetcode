<h2><a href="https://leetcode.com/problems/contains-duplicate-ii">Contains Duplicate II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> if there are two <strong>distinct indices</strong> <code>i</code> and <code>j</code> in the array such that <code>nums[i] == nums[j]</code> and <code>|i - j| &lt;= k</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,3,1], k = 3
Output: true
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,0,1,1], k = 1
Output: true
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 10<sup>5</sup></li>
  <li>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></li>
  <li>0 &lt;= k &lt;= 10<sup>5</sup></li>
</ul>

---

### Solution

**Approach:**  
Use a dictionary to store the most recent index of each value.  
For every number, check if it already appeared and if the index difference is within <code>k</code>.

**Complexity:**  
- Time: O(n)  
- Space: O(n)

---
