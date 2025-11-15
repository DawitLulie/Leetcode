<h2><a href="https://leetcode.com/problems/intersection-of-two-arrays">Intersection of Two Arrays</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return an array of their intersection. Each element in the result must be <strong>unique</strong> and you may return the result in <strong>any order</strong>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums1.length, nums2.length &lt;= 1000</li>
  <li>0 &lt;= nums1[i], nums2[i] &lt;= 1000</li>
</ul>

---

### Solution

**Approach:**  
Convert both arrays to sets.  
Then return the intersection of the two sets.

**Complexity:**  
- Time: O(n + m)  
- Space: O(n + m)
