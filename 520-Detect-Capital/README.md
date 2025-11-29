<h2><a href="https://leetcode.com/problems/detect-capital">Detect Capital</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>We define the usage of capitals in a word to be correct when one of the following cases holds:</p>

<ul>
  <li>All letters are uppercase. (e.g., "USA")</li>
  <li>All letters are lowercase. (e.g., "leetcode")</li>
  <li>Only the first letter is uppercase and the rest are lowercase. (e.g., "Google")</li>
</ul>

<p>Given a string <code>word</code>, return <code>true</code> if the usage of capitals is correct.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: word = "USA"
Output: true
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: word = "FlaG"
Output: false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= word.length &lt;= 100</li>
  <li>word consists of lowercase and uppercase English letters.</li>
</ul>

---

### Solution

**Approach:**  
There are only three valid capital patterns:

1. Entire word uppercase  
2. Entire word lowercase  
3. First letter uppercase + rest lowercase  

Check each condition directly using built-in string functions.

**Complexity:**  
- Time: **O(n)**  
- Space: **O(1)**

---
