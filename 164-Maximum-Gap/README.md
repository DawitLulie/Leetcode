<h2><a href="https://leetcode.com/problems/maximum-gap">Maximum Gap</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>Given an integer array <code>nums</code>, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.</p>

<p>You must write an algorithm that runs in linear time and uses linear extra space.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted array is [1,3,6,9], maximum gap is 6-3 = 3.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [10]
Output: 0
Explanation: The array contains less than two elements.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 10<sup>5</sup></li>
  <li>0 &lt;= nums[i] &lt;= 10<sup>9</sup></li>
</ul>

---

### Solution

**Approach:**  
1. If the array has less than 2 elements, return 0.  
2. Sort the array.  
3. Iterate through the sorted array and calculate the difference between consecutive elements.  
4. Keep track of the maximum difference.  
5. Return the maximum difference found.  

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1)
