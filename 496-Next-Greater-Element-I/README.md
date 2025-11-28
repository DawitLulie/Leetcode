<h2><a href="https://leetcode.com/problems/next-greater-element-i">496. Next Greater Element I</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code> where <code>nums1</code> is a subset of <code>nums2</code>.  
For each element in <code>nums1</code>, find the next greater element in <code>nums2</code>.  
The next greater element of a number <code>x</code> in <code>nums2</code> is the first number to the right of <code>x</code> that is greater than <code>x</code>. If it does not exist, return <code>-1</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 &lt;= nums1.length &lt;= nums2.length &lt;= 1000</code></li>
  <li><code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>4</sup></code></li>
  <li>All elements in <code>nums1</code> and <code>nums2</code> are unique.</li>
  <li>All elements of <code>nums1</code> appear in <code>nums2</code>.</li>
</ul>

---

### Solution

**Approach:**  
Use a stack to keep track of elements while scanning `nums2`.  
Map each number to its next greater element.  
Then look up the answer for elements in `nums1`.

**Complexity:**  
- Time: O(n + m) (n = len(nums2), m = len(nums1))  
- Space: O(n)

---
