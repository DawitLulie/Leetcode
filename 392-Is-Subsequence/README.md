<h2><a href="https://leetcode.com/problems/is-subsequence">392. Is Subsequence</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>s</code> is a subsequence of <code>t</code>, or <code>false</code> otherwise.</p>

<p>A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "abc", t = "ahbgdc"
Output: true
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "axc", t = "ahbgdc"
Output: false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>0 &lt;= s.length &lt;= 100</code></li>
  <li><code>0 &lt;= t.length &lt;= 10<sup>4</sup></code></li>
  <li><code>s</code> and <code>t</code> consist only of lowercase English letters.</li>
</ul>

---

### Solution

**Approach:**  
Use two pointers.  
Move through both strings and match characters one-by-one.  
If all characters in <code>s</code> are matched in order, return <code>true</code>.

**Complexity:**  
- Time: O(n + m)  
- Space: O(1)

---
