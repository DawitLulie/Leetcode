<h2><a href="https://leetcode.com/problems/merge-sorted-array">Merge Sorted Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given two sorted integer arrays <code>nums1</code> and <code>nums2</code>, merge <code>nums2</code> into <code>nums1</code> as one sorted array. The number of elements initialized in <code>nums1</code> and <code>nums2</code> are <code>m</code> and <code>n</code> respectively. You may assume that <code>nums1</code> has enough space (size that is greater or equal to m + n) to hold additional elements from <code>nums2</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>nums1.length == m + n</li>
  <li>nums2.length == n</li>
  <li>0 &lt;= m, n &lt;= 200</li>
  <li>1 &lt;= m + n &lt;= 200</li>
  <li>-10<sup>9</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>9</sup></li>
</ul>

---

### Solution

**Approach:**  
Merge arrays from the end:
1. Initialize three pointers: `i = m - 1`, `j = n - 1`, `k = m + n - 1`.  
2. Compare `nums1[i]` and `nums2[j]`, place the larger at `nums1[k]` and move pointers accordingly.  
3. After one array is exhausted, copy remaining elements from `nums2` if any.  

**Time Complexity:** O(m + n)  
**Space Complexity:** O(1)
