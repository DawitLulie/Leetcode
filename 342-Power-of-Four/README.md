<h2><a href="https://leetcode.com/problems/power-of-four">Power of Four</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer <code>n</code>, return <code>true</code> if it is a power of four. Otherwise, return <code>false</code>.</p>

<p>An integer <code>n</code> is a power of four if there exists an integer <code>x</code> such that <code>n == 4<sup>x</sup></code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: n = 16
Output: true
Explanation: 4^2 = 16
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: n = 5
Output: false
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: n = 1
Output: true
Explanation: 4^0 = 1
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</li>
</ul>

---

### Solution

**Approach:**  
First, check if the number is a power of two.  
Then, ensure that the single 1-bit is in an even position to satisfy power of four.  
Use bitmask 0x55555555 to verify the position.

**Complexity:**  
- Time: O(1)  
- Space: O(1)

---
