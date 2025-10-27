<h2><a href="https://leetcode.com/problems/first-missing-positive">First Missing Positive</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>Given an unsorted integer array <code>nums</code>, find the smallest missing positive integer.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,0]
Output: 3
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [3,4,-1,1]
Output: 2
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [7,8,9,11,12]
Output: 1
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>0 &lt;= nums.length &lt;= 5 * 10<sup>5</sup></li>
  <li>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</li>
</ul>

---

### Solution

**Approach:**  
Use **cyclic sort** to place each number in its correct position (i.e., `num` should be at index `num - 1`) if possible:

1. Iterate through the array, swapping numbers to their correct positions.  
2. After rearranging, iterate again to find the first index `i` where `nums[i] != i + 1`.  
3. Return `i + 1` as the first missing positive.  
4. If all positions are correct, return `n + 1`.  

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
