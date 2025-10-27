<h2><a href="https://leetcode.com/problems/plus-one">Plus One</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a non-empty array of decimal digits representing a non-negative integer, increment the integer by one. The digits are stored such that the most significant digit is at the head of the list, and each element contains a single digit.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: 123 + 1 = 124
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: digits = [9]
Output: [1,0]
Explanation: 9 + 1 = 10
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= digits.length &lt;= 100</li>
  <li>0 &lt;= digits[i] &lt;= 9</li>
  <li>digits does not contain leading zeros except for the zero itself.</li>
</ul>

---

### Solution

**Approach:**  
Iterate from the last digit backwards. If a digit is less than 9, increment it and return. If it is 9, set it to 0 and continue. If all digits are 9, add a new 1 at the front.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
