<h2><a href="https://leetcode.com/problems/wiggle-sort-ii">Wiggle Sort II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code>, reorder it in-place such that <code>nums[0] &lt; nums[1] &gt; nums[2] &lt; nums[3]...</code></p>

<p>You may assume the input always has a valid answer.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></li>
  <li>0 &lt;= nums[i] &lt;= 5000</li>
  <li>It is guaranteed that there will be an answer for the given input nums.</li>
</ul>

---

### Solution

**Approach:**  
Sort the array first.  
Split it into two halves and reverse both halves.  
Place the smaller half at even indices and the larger half at odd indices to satisfy the wiggle property.

**Complexity:**  
- Time: O(n log n)  
- Space: O(n)

---
