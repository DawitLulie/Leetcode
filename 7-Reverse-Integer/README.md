<h2><a href="https://leetcode.com/problems/reverse-integer">Reverse Integer</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a signed 32-bit integer <code>x</code>, return <em>the number formed by reversing its digits</em>.</p>

<p>If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range: <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: x = 123
Output: 321
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: x = -123
Output: -321
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: x = 120
Output: 21
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1</code></li>
</ul>

---

### Solution

**Approach:**  
Convert the integer to string and reverse it.  
If the reversed number goes beyond the allowed 32-bit integer range, return <code>0</code>.

**Complexity:**  
- Time: <code>O(n)</code>, where <code>n</code> is number of digits  
- Space: <code>O(n)</code>
