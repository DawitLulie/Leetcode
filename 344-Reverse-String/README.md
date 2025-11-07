<h2><a href="https://leetcode.com/problems/reverse-string">Reverse String</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Write a function that reverses a string. The input string is given as an array of characters <code>s</code>.</p>

<p>You must do this by modifying the input array in-place with O(1) extra memory.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= s.length &lt;= 10<sup>5</sup></li>
  <li><code>s[i]</code> is a printable ascii character.</li>
</ul>

---

### Solution

**Approach:**  
Use two pointers, one starting at the beginning and one at the end of the array.  
Swap the characters and move the pointers toward each other until they meet.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---
