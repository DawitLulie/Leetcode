<h2><a href="https://leetcode.com/problems/intersection-of-two-arrays-ii">Intersection of Two Arrays II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return an array of their intersection. Each element in the result should appear as many times as it shows in both arrays, and you may return the result in <strong>any order</strong>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums1.length, nums2.length &lt;= 1000</li>
  <li>0 &lt;= nums1[i], nums2[i] &lt;= 1000</li>
</ul>

<p><strong>Follow-up:</strong></p>
<ul>
  <li>What if the given arrays are already sorted? How would you optimize your solution?</li>
  <li>What if <code>nums1</code> is much smaller than <code>nums2</code>? What if <code>nums2</code> is much smaller than <code>nums1</code>?</li>
</ul>

---

### Solution

**Approach:**  
Use a dictionary to count elements of <code>nums1</code>.  
Iterate through <code>nums2</code> and add matching elements while decreasing counts.

**Complexity:**  
- Time: O(n + m)  
- Space: O(n)
