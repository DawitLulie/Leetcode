<h2><a href="https://leetcode.com/problems/single-number">Single Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a non-empty array of integers <code>nums</code>, every element appears twice except for one. Find that single one.</p>

<p>You must implement a solution with a linear runtime complexity and use only constant extra space.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [2,2,1]
Output: 1
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [4,1,2,1,2]
Output: 4
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [1]
Output: 1
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></li>
  <li>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></li>
  <li>Each element appears **exactly twice** except for one element which appears once.</li>
</ul>

---

### Solution

**Approach:**  
1. Initialize a variable `result` to 0.  
2. XOR each number in the array with `result`.  
3. The duplicate numbers cancel out because `a ^ a = 0`.  
4. Return `result`, which contains the single number.  

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
