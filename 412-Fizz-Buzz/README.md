<h2><a href="https://leetcode.com/problems/fizz-buzz">412. Fizz Buzz</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer <code>n</code>, return a string array <code>answer</code> (1-indexed) where:</p>
<ul>
  <li><code>answer[i] == "FizzBuzz"</code> if <code>i</code> is divisible by 3 and 5.</li>
  <li><code>answer[i] == "Fizz"</code> if <code>i</code> is divisible by 3.</li>
  <li><code>answer[i] == "Buzz"</code> if <code>i</code> is divisible by 5.</li>
  <li><code>answer[i] == i</code> (as a string) if none of the above conditions are true.</li>
</ul>

<p><strong>Example 1:</strong></p>
<pre>
Input: n = 3
Output: ["1","2","Fizz"]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

---

### Solution

**Approach:**  
Loop from 1 to <code>n</code>.  
Check divisibility by both 3 and 5, then 3, then 5.  
Append the correct word or number as a string.

**Complexity:**  
- Time: O(n)  
- Space: O(1) (ignoring output list)

---
