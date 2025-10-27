<h2><a href="https://leetcode.com/problems/search-insert-position">Search Insert Position</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a sorted array of distinct integers <code>nums</code> and a target value <code>target</code>, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,3,5,6], target = 5
Output: 2
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,3,5,6], target = 2
Output: 1
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [1,3,5,6], target = 7
Output: 4
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 10<sup>4</sup></li>
  <li>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></li>
  <li>nums contains **distinct** values sorted in ascending order.</li>
  <li>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></li>
</ul>

---

### Solution

**Approach:**  
Use **binary search** to find the target efficiently in a sorted array.  

1. Initialize `left` and `right` pointers.  
2. While `left <= right`:
   - Calculate `mid` as `(left + right) // 2`.  
   - If `nums[mid] == target`, return `mid`.  
   - If `nums[mid] < target`, move `left` to `mid + 1`.  
   - If `nums[mid] > target`, move `right` to `mid - 1`.  
3. If target is not found, return `left` as the insertion position.

**Time Complexity:** O(log n)  
**Space Complexity:** O(1)
