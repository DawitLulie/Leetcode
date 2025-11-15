<h2><a href="https://leetcode.com/problems/valid-perfect-square">Valid Perfect Square</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a positive integer <code>num</code>, return <code>true</code> if <code>num</code> is a perfect square, otherwise return <code>false</code>.</p>

<p>You must not use any built-in library function such as <code>sqrt</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: num = 16
Output: true
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: num = 14
Output: false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= num &lt;= 2<sup>31</sup> - 1</li>
</ul>

---

### Solution

**Approach:**  
Use binary search from <code>1</code> to <code>num</code>.  
For each mid, check if <code>mid * mid</code> equals <code>num</code>.  
Adjust the search range accordingly.

**Complexity:**  
- Time: O(log n)  
- Space: O(1)
