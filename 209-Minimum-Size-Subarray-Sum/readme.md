<h2><a href="https://leetcode.com/problems/minimum-size-subarray-sum">209. Minimum Size Subarray Sum</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>Given an array of positive integers <code>nums</code> and a positive integer <code>target</code>, return the minimal length of a subarray whose sum is greater than or equal to <code>target</code>. If there is no such subarray, return <code>0</code> instead.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: target = 4, nums = [1,4,4]
Output: 1
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= target &lt;= 10<sup>9</sup></li>
  <li>1 &lt;= nums.length &lt;= 10<sup>5</sup></li>
  <li>1 &lt;= nums[i] &lt;= 10<sup>4</sup></li>
</ul>

---

### Solution

**Approach:**  
Use the **sliding window technique**.  
- Expand the right pointer and add elements to the current sum.  
- Once the sum ≥ target, move the left pointer to minimize the window size.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---
