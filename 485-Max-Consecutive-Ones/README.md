<h2><a href="https://leetcode.com/problems/max-consecutive-ones">485. Max Consecutive Ones</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a binary array <code>nums</code>, return the maximum number of consecutive <code>1</code>'s in the array.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The longest sequence of consecutive ones is [1,1,1].
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,0,1,1,0,1]
Output: 2
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

---

### Solution

**Approach:**  
Scan the array once and count how many `1`s appear in a row.  
Whenever you see a `0`, reset the current count.  
Track the maximum streak seen so far.

**Complexity:**  
- Time: **O(n)**  
- Space: **O(1)**

---
