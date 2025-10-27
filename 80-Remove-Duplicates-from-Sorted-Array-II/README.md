<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii">Remove Duplicates from Sorted Array II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>Given a sorted array <code>nums</code>, remove the duplicates in-place such that duplicates appear **at most twice** and return the new length. Do not allocate extra space for another array.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,1,1,2,2,3]
Output: 5
Explanation: The array becomes [1,1,2,2,3]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7
Explanation: The array becomes [0,0,1,1,2,3,3]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></li>
  <li>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></li>
  <li>nums is sorted in non-decreasing order.</li>
</ul>

---

### Solution

**Approach:**  
Use a two-pointer approach:
1. Keep `index` to track the position to insert a new element.  
2. Start iterating from the third element.  
3. If `nums[i]` is not equal to `nums[index - 2]`, insert it at `index` and increment `index`.  
4. Return `index` as the new length.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
