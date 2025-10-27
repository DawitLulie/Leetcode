<h2><a href="https://leetcode.com/problems/number-of-1-bits">Number of 1 Bits</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: There are three '1' bits.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: n = 00000000000000000000000010000000
Output: 1
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: n = 11111111111111111111111111111101
Output: 31
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>The input must be a **binary string of length 32**.</li>
</ul>

---

### Solution

**Approach:**  
1. Initialize `count` to 0.  
2. While `n` is not zero, add `n & 1` to `count`.  
3. Right-shift `n` by 1.  
4. Return `count`.  

**Time Complexity:** O(1)  
**Space Complexity:** O(1)
