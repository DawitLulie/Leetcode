<h2><a href="https://leetcode.com/problems/sqrtx">Sqrt(x)</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a non-negative integer <code>x</code>, return the integer part of the square root of <code>x</code>. You must not use any built-in exponent function or operator.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: x = 4
Output: 2
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: x = 8
Output: 2
Explanation: The square root of 8 is approximately 2.82842, and since we want the integer part, we return 2.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>0 &lt;= x &lt;= 2<sup>31</sup> - 1</li>
</ul>

---

### Solution

**Approach:**  
Use binary search between 1 and x//2 to find the integer square root:  

1. Initialize `left` = 1 and `right` = x // 2.  
2. While `left <= right`:  
   - Compute `mid = (left + right) // 2`.  
   - If `mid * mid == x`, return `mid`.  
   - If `mid * mid < x`, move `left` to `mid + 1`.  
   - Otherwise, move `right` to `mid - 1`.  
3. Return `right` as the integer square root.

**Time Complexity:** O(log x)  
**Space Complexity:** O(1)
