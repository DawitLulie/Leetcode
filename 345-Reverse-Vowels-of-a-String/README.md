<h2><a href="https://leetcode.com/problems/reverse-vowels-of-a-string">Reverse Vowels of a String</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a string <code>s</code>, reverse only all the vowels in the string and return it.</p>

<p>The vowels are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, <code>'u'</code>, and they can appear in uppercase or lowercase.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "hello"
Output: "holle"
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "leetcode"
Output: "leotcede"
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></li>
  <li><code>s</code> consists of printable ASCII characters.</li>
</ul>

---

### Solution

**Approach:**  
Use two pointers to scan from both ends.  
Swap characters only if both are vowels, otherwise move pointers.  
Reconstruct the string after all swaps.

**Complexity:**  
- Time: O(n)  
- Space: O(n) (to convert string to list)

---
