<h2><a href="https://leetcode.com/problems/sort-characters-by-frequency">451. Sort Characters By Frequency</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a string <code>s</code>, sort it in <strong>decreasing order</strong> based on the <strong>frequency</strong> of the characters. The frequency of a character is the number of times it appears in the string.</p>

<p>Return the sorted string.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "tree"
Output: "eetr"
Explanation: 'e' appears twice while 't' and 'r' both appear once.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "cccaaa"
Output: "cccaaa"
Explanation: 'c' and 'a' both appear three times.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: s = "Aabb"
Output: "bbAa"
Explanation: 'b' appears twice, 'A' and 'a' both appear once.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
  <li><code>s</code> consists of uppercase and lowercase English letters and digits.</li>
</ul>

---

### Solution

**Approach:**  
Use a dictionary to count the frequency of each character.  
Sort the characters based on frequency (descending).  
Build the result string by repeating each character according to its frequency.

**Complexity:**  
- Time: O(n log n)  
- Space: O(n)

---
