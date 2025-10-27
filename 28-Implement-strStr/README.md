<h2><a href="https://leetcode.com/problems/implement-strstr">Implement strStr()</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Implement the <code>strStr()</code> function, which finds the index of the first occurrence of the substring <code>needle</code> in the string <code>haystack</code>, or returns <code>-1</code> if <code>needle</code> is not part of <code>haystack</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: haystack = "hello", needle = "ll"
Output: 2
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: haystack = "aaaaa", needle = "bba"
Output: -1
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: haystack = "", needle = ""
Output: 0
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>0 &lt;= haystack.length, needle.length &lt;= 5 * 10^4</li>
  <li>haystack and needle consist of only lowercase English characters.</li>
</ul>

---

### Solution

**Approach:**  
Use a sliding window approach: iterate through `haystack` and at each index, check if the substring of length `needle` matches `needle`.  

**Time Complexity:** O(n * m)  
**Space Complexity:** O(1)
