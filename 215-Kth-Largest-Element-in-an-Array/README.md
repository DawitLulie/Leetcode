<h2><a href="https://leetcode.com/problems/kth-largest-element-in-an-array">215. Kth Largest Element in an Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the <code>k<sup>th</sup></code> largest element in the array.</p>

<p>Note that it is the <strong>k<sup>th</sup></strong> largest element in the sorted order, not the <strong>k<sup>th</sup></strong> distinct element.</p>

<p>You must solve it in <code>O(n log k)</code> time complexity.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></li>
  <li>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></li>
</ul>

---

### Solution

**Approach:**  
Use a **min-heap** of size <code>k</code>.  
Keep the largest <code>k</code> elements in the heap — the smallest among them (the heap root) is the k-th largest.

**Complexity:**  
- Time: O(n log k)  
- Space: O(k)

---
