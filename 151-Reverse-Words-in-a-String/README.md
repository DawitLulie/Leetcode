<h2><a href="https://leetcode.com/problems/reverse-words-in-a-string">Reverse Words in a String</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>Given an input string <code>s</code>, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in <code>s</code> will be separated by at least one space.</p>

<p>Return a string of the words in reverse order concatenated by a single space. Note that <strong>your reversed string should not contain leading or trailing spaces</strong>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "the sky is blue"
Output: "blue is sky the"
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= s.length &lt;= 10<sup>4</sup></li>
  <li><code>s</code> contains English letters (upper-case and lower-case), digits, and spaces <code>' '</code>.</li>
  <li>There is at least one word in <code>s</code>.</li>
</ul>

---

### Solution

**Approach:**  
1. Split the string into words using a string stream.  
2. Store words in a vector.  
3. Reverse the vector of words.  
4. Join words with a single space to form the final string.  

**Time Complexity:** O(n)  
**Space Complexity:** O(n)
