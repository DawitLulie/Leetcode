<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array">Remove Duplicates from Sorted Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a sorted array <code>nums</code>, remove the duplicates in-place such that each element appears only once and returns the new length.</p>

<p>Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></li>
  <li>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></li>
  <li>nums is sorted in ascending order.</li>
</ul>

---

### Solution

**Approach:**  
Use two pointers: one for reading and one for writing. Copy only unique elements to the write position.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---
