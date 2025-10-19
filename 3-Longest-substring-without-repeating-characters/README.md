<h2><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters">Longest Substring Without Repeating Characters</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a string <code>s</code>, find the length of the longest substring without repeating characters.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></li>
  <li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>

<p><strong>Follow-up:</strong> Can you solve it in O(n) time complexity?</p>

---

### Solution

**Approach:**  
Use a sliding window with a dictionary to store the last index of each character.  
Move the left boundary of the window when a repeated character is found.

**Complexity:**  
- Time: O(n)  
- Space: O(n)

---
