<h2><a href="https://leetcode.com/problems/palindrome-number">Palindrome Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer <code>x</code>, return <code>true</code> if <code>x</code> is a palindrome, and <code>false</code> otherwise.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: x = 121
Output: true
Explanation: 121 reads the same forward and backward.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: x = -121
Output: false
Explanation: Reads -121 backward as 121-, which is not the same.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: x = 10
Output: false
Explanation: Reads 01 backward, which is not the same.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>-2<sup>31</sup> ≤ x ≤ 2<sup>31</sup> - 1</li>
</ul>

<p><strong>Follow-up:</strong> Could you solve it without converting the integer to a string?</p>

---

### Solution

**Approach:**  
Reverse the number mathematically and compare it with the original number.

**Complexity:**  
- Time: O(log10(n))  
- Space: O(1)

---
