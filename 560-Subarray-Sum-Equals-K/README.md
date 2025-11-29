<h2><a href="https://leetcode.com/problems/subarray-sum-equals-k">Subarray Sum Equals K</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the number of continuous subarrays whose sum equals <code>k</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,1,1], k = 2
Output: 2
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,2,3], k = 3
Output: 2
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></li>
  <li>-1000 &lt;= nums[i] &lt;= 1000</li>
  <li>-10<sup>7</sup> &lt;= k &lt;= 10<sup>7</sup></li>
</ul>

---

### Solution

**Approach:**  
Use a prefix sum and a dictionary to count how many times each cumulative sum appears.  
If `current_sum - k` exists in the dictionary, add its count to the answer.

**Complexity:**  
- Time: **O(n)**  
- Space: **O(n)**

---
