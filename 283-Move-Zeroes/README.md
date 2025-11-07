<h2><a href="https://leetcode.com/problems/move-zeroes">Move Zeroes</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code>, move all 0's to the end of it while maintaining the relative order of the non-zero elements.</p>

<p>Note that you must do this in-place without making a copy of the array.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [0]
Output: [0]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 10<sup>4</sup></li>
  <li>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</li>
</ul>

---

### Solution

**Approach:**  
Use a pointer to track the position of the last non-zero element.  
Swap non-zero elements forward, moving all zeros to the end.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---
