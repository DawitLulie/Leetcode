<h2><a href="https://leetcode.com/problems/sort-colors">Sort Colors</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>Given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We use the integers 0, 1, and 2 to represent the colors red, white, and blue, respectively.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [2,0,1]
Output: [0,1,2]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>n == nums.length</code></li>
  <li><code>1 &lt;= n &lt;= 300</code></li>
  <li><code>nums[i]</code> is either 0, 1, or 2.</li>
</ul>

---

### Solution

**Approach:**  
Implement the Dutch National Flag algorithm using three pointers:
- `low`: Tracks the next position for 0.
- `mid`: Current element being examined.
- `high`: Tracks the next position for 2.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
