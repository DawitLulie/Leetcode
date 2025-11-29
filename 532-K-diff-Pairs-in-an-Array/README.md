<h2><a href="https://leetcode.com/problems/k-diff-pairs-in-an-array">K-diff Pairs in an Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the number of unique k-diff pairs in the array.</p>

<p>A k-diff pair is an integer pair <code>(nums[i], nums[j])</code>, where:</p>
<ul>
  <li>0 &lt;= i &lt; j &lt; nums.length</li>
  <li>|nums[i] - nums[j]| == k</li>
</ul>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: The pairs are (1,3) and (3,5).
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: The pairs are (1,2), (2,3), (3,4), (4,5).
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: Only the pair (1,1) exists.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 10<sup>4</sup></li>
  <li>-10<sup>7</sup> &lt;= nums[i] &lt;= 10<sup>7</sup></li>
  <li>0 &lt;= k &lt;= 10<sup>7</sup></li>
</ul>

---

### Solution

**Approach:**  
Use a set to track unique numbers.  
If k > 0, check if `num + k` exists in the set.  
If k == 0, count numbers that appear at least twice.

**Complexity:**  
- Time: **O(n)**  
- Space: **O(n)**

---
