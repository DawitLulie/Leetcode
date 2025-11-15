<h2><a href="https://leetcode.com/problems/ransom-note">Ransom Note</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given two strings <code>ransomNote</code> and <code>magazine</code>, return <code>true</code> if <code>ransomNote</code> can be constructed by using the letters from <code>magazine</code>, and <code>false</code> otherwise.</p>

<p>Each letter in <code>magazine</code> can only be used once in <code>ransomNote</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: ransomNote = "a", magazine = "b"
Output: false
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: ransomNote = "aa", magazine = "ab"
Output: false
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: ransomNote = "aa", magazine = "aab"
Output: true
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= ransomNote.length, magazine.length &lt;= 10<sup>5</sup></li>
  <li><code>ransomNote</code> and <code>magazine</code> consist of lowercase English letters.</li>
</ul>

---

### Solution

**Approach:**  
Use a dictionary to count the characters in <code>magazine</code>.  
Decrease the count while checking each character in <code>ransomNote</code>.  
If any character is missing or insufficient, return false.

**Complexity:**  
- Time: O(n + m)  
- Space: O(m)
