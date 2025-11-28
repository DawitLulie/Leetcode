<h2><a href="https://leetcode.com/problems/fibonacci-number">509. Fibonacci Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>The Fibonacci numbers, commonly denoted <code>F(n)</code> form a sequence, where each number is the sum of the two preceding ones, starting from <code>F(0) = 0</code> and <code>F(1) = 1</code>.</p>

<p>Given <code>n</code>, calculate <code>F(n)</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>0 &lt;= n &lt;= 30</code></li>
</ul>

---

### Solution

**Approach:**  
Use an iterative approach with two variables to store previous Fibonacci numbers.  
Calculate Fibonacci up to n efficiently.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---
