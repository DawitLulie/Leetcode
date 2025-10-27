<h2><a href="https://leetcode.com/problems/length-of-last-word">Length of Last Word</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a string <code>s</code> consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= s.length &lt;= 10<sup>4</sup></li>
  <li>s consists of only English letters and spaces <code>' '</code>.</li>
  <li>There will be at least one word in <code>s</code>.</li>
</ul>

---

### Solution

**Approach:**  
Start from the end of the string and move backwards to find the last word. Skip any trailing spaces, then count the characters of the last word until a space is encountered.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
