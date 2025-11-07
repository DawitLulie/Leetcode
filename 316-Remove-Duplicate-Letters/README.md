<h2><a href="https://leetcode.com/problems/remove-duplicate-letters">Remove Duplicate Letters</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a string <code>s</code>, remove duplicate letters so that every letter appears **once and only once**. You must make sure your result is **the smallest in lexicographical order** among all possible results.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "bcabc"
Output: "abc"
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "cbacdcbc"
Output: "acdb"
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= s.length &lt;= 10<sup>4</sup></li>
  <li><code>s</code> consists of lowercase English letters.</li>
</ul>

---

### Solution

**Approach:**  
Use a stack to build the result string.  
Keep track of letters already in the stack with a set.  
Remove letters from the stack if the current letter is smaller and the removed letter appears later.

**Complexity:**  
- Time: O(n)  
- Space: O(26) ~ O(1)

---
