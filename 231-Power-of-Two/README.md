<h2><a href="https://leetcode.com/problems/power-of-two">Power of Two</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer <code>n</code>, return <code>true</code> if it is a power of two. Otherwise, return <code>false</code>.</p>

<p>An integer <code>n</code> is a power of two if there exists an integer <code>x</code> such that <code>n == 2<sup>x</sup></code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: n = 1
Output: true
Explanation: 2^0 = 1
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: n = 16
Output: true
Explanation: 2^4 = 16
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: n = 3
Output: false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</li>
</ul>

---

### Solution

**Approach:**  
A number is a power of two if it has exactly one bit set.  
Using the expression <code>n & (n - 1)</code> removes the lowest set bit.  
If the result becomes zero, it is a power of two.

**Complexity:**  
- Time: O(1)  
- Space: O(1)

---
