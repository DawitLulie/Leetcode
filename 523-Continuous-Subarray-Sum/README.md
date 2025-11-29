<h2><a href="https://leetcode.com/problems/continuous-subarray-sum">Continuous Subarray Sum</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> if <code>nums</code> has a continuous subarray of size at least 2 whose elements sum up to a multiple of <code>k</code>. Otherwise, return <code>false</code>.</p>

<p>A continuous subarray is a subarray that appears in the original array without gaps.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [23, 2, 4, 6, 7], k = 6
Output: true
Explanation: The subarray [2, 4] has sum 6, which is a multiple of 6.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [23, 2, 6, 4, 7], k = 6
Output: true
Explanation: The subarray [23, 2, 6] has sum 31, which is a multiple of 6.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [23, 2, 6, 4, 7], k = 13
Output: false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 10<sup>5</sup></li>
  <li>0 &lt;= nums[i] &lt;= 10<sup>9</sup></li>
  <li>0 &lt;= k &lt;= 2 * 10<sup>9</sup></li>
</ul>

---

### Solution

**Approach:**  
Use prefix sums and check remainders when divided by <code>k</code>.  
If the same remainder appears again and the distance between indices is at least 2, the subarray sum is a multiple of <code>k</code>.

This works because:  
If `(prefix[j] - prefix[i]) % k == 0`, then the subarray sum between them is divisible by `k`.

**Complexity:**
- Time: **O(n)**
- Space: **O(n)**

---
