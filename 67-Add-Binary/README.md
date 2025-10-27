<h2><a href="https://leetcode.com/problems/add-binary">Add Binary</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given two binary strings <code>a</code> and <code>b</code>, return their sum as a binary string.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: a = "11", b = "1"
Output: "100"
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: a = "1010", b = "1011"
Output: "10101"
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></li>
  <li><code>a</code> and <code>b</code> consist only of '0' or '1' characters.</li>
  <li>Each string is non-empty.</li>
</ul>

---

### Solution

**Approach:**  
Perform binary addition from right to left, keeping track of a carry.  
At each step, add digits from `a` and `b` if available, plus the carry.  
Append the least significant bit to the result and update the carry.  
Finally, reverse the result list to get the correct binary string.

**Time Complexity:** O(max(n, m))  
**Space Complexity:** O(max(n, m))
