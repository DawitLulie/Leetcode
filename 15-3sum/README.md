<h2><a href="https://leetcode.com/problems/3sum">3Sum</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code>, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that:</p>

<ul>
  <li>i, j, k are distinct indices, and</li>
  <li>nums[i] + nums[j] + nums[k] == 0</li>
</ul>

<p>The solution set must not contain duplicate triplets.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = []
Output: []
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [0]
Output: []
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>0 &lt;= nums.length &lt;= 3000</li>
  <li>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></li>
</ul>

<p><strong>Follow-up:</strong> Could you solve it with better than O(n³) time complexity?</p>

---

### Solution

**Approach:**  
Sort the array and use a two-pointer technique for each number to find pairs that sum to its negative.  
Skip duplicates to ensure unique triplets.

**Complexity:**  
- Time: O(n²)  
- Space: O(1) extra (ignoring output storage)

---
