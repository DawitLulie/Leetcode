<h2><a href="https://leetcode.com/problems/first-unique-character-in-a-string">First Unique Character in a String</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />
<hr>

<p>Given a string <code>s</code>, return the index of the first non-repeating character in it. If it does not exist, return <code>-1</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "leetcode"
Output: 0
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "loveleetcode"
Output: 2
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: s = "aabb"
Output: -1
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ s.length ≤ 10<sup>5</sup></li>
  <li><code>s</code> consists of only lowercase English letters.</li>
</ul>

<hr>

<h3>Solution</h3>

<p><strong>Approach:</strong><br>
Count the frequency of each character using a dictionary.  
Then scan the string again and return the first index whose character count is <code>1</code>.
</p>

<p><strong>Complexity:</strong></p>
<ul>
  <li>Time: <code>O(n)</code></li>
  <li>Space: <code>O(1)</code> (because the alphabet size is fixed)</li>
</ul>
