<h2><a href="https://leetcode.com/problems/rotate-array">Rotate Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>Given an array, rotate the array to the right by <code>k</code> steps, where <code>k</code> is non-negative.</p>

<p>You must do this in-place with O(1) extra space.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 10<sup>5</sup></li>
  <li>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup>-1</li>
  <li>0 &lt;= k &lt;= 10<sup>5</sup></li>
</ul>

---

### Solution

**Approach:**  
1. Reduce k modulo n to handle cases where k &gt; n.  
2. Reverse the entire array.  
3. Reverse the first k elements.  
4. Reverse the remaining n-k elements.  

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
