<h2><a href="https://leetcode.com/problems/two-sum">Two Sum</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an array of integers <code>nums</code> and an integer <code>target</code>, return indices of the two numbers such that they add up to <code>target</code>.</p>

<p>You may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice.</p>

<p>You can return the answer in any order.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [3,2,4], target = 6
Output: [1,2]
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [3,3], target = 6
Output: [0,1]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>2 &lt;= nums.length &lt;= 10<sup>4</sup></li>
  <li>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></li>
  <li>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></li>
  <li>Only one valid answer exists.</li>
</ul>

<p><strong>Follow-up:</strong> Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code> time complexity?</p>

---

### Solution

**Approach:**  
Use a dictionary to store each number’s index.  
For every number, check if the complement (`target - number`) exists in the dictionary.

**Complexity:**  
- Time: O(n)  
- Space: O(n)

---
