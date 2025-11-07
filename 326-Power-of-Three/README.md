<h2><a href="https://leetcode.com/problems/power-of-three">Power of Three</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer <code>n</code>, return <code>true</code> if it is a power of three. Otherwise, return <code>false</code>.</p>

<p>An integer <code>n</code> is a power of three if there exists an integer <code>x</code> such that <code>n == 3<sup>x</sup></code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: n = 27
Output: true
Explanation: 3^3 = 27
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: n = 0
Output: false
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: n = 9
Output: true
Explanation: 3^2 = 9
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</li>
</ul>

---

### Solution

**Approach:**  
Divide the number by 3 repeatedly as long as it is divisible.  
If the final result is 1, the number is a power of three.

**Complexity:**  
- Time: O(log₃ n)  
- Space: O(1)

---
