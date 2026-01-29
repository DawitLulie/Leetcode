<h2>
  <a href="https://leetcode.com/problems/happy-number">
    Happy Number
  </a>
</h2>

<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />
<hr>

<p>
Write an algorithm to determine if a number <code>n</code> is happy.
</p>

<p>
A happy number is defined by the following process:
</p>

<ul>
  <li>Starting with any positive integer, replace the number by the sum of the squares of its digits.</li>
  <li>Repeat the process until the number equals 1 (where it will stay), or it loops endlessly.</li>
</ul>

<p>
Return <code>true</code> if <code>n</code> is a happy number, and <code>false</code> if not.
</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: n = 19
Output: true
Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: n = 2
Output: false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ n ≤ 2³¹ - 1</li>
</ul>

---

### Solution

<strong>Approach:</strong><br>
Use a set to track numbers already seen.  
If the number repeats, a loop exists → not happy.

<strong>Complexity:</strong>
<ul>
  <li>Time: O(log n)</li>
  <li>Space: O(log n)</li>
</ul>

---
