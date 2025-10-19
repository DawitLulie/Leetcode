<h2><a href="https://leetcode.com/problems/valid-parentheses">Valid Parentheses</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a string <code>s</code> containing just the characters <code>'(', ')', '{', '}', '['</code>, and <code>']'</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>
<ul>
  <li>Open brackets are closed by the same type of brackets.</li>
  <li>Open brackets are closed in the correct order.</li>
</ul>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "()"
Output: true
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "()[]{}"
Output: true
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: s = "(]"
Output: false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= s.length &lt;= 10<sup>4</sup></li>
  <li><code>s</code> consists of parentheses only <code>'()[]{}'</code>.</li>
</ul>

---

### Solution

**Approach:**  
Use a stack to track open brackets. For each closing bracket, check if it matches the top of the stack.

**Complexity:**  
- Time: O(n)  
- Space: O(n)

---
