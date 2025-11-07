<h2><a href="https://leetcode.com/problems/majority-element-ii">Majority Element II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code>, return all the elements that appear more than <code>⌊ n/3 ⌋</code> times.</p>

<p>The algorithm should run in linear time and in O(1) space.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [3,2,3]
Output: [3]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1]
Output: [1]
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [1,2]
Output: [1,2]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></li>
  <li>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></li>
</ul>

---

### Solution

**Approach:**  
Use the extended Boyer–Moore majority vote algorithm.  
Track two possible majority candidates and verify them at the end.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---
