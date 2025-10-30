<h2><a href="https://leetcode.com/problems/contains-duplicate">217. Contains Duplicate</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears at least twice in the array, and return <code>false</code> if every element is distinct.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,3,1]
Output: true
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,2,3,4]
Output: false
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 10<sup>5</sup></li>
  <li>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></li>
</ul>

---

### Solution

**Approach:**  
Use a <code>set</code> to check for duplicates efficiently.  
If the length of the set is smaller than the list, it means duplicates exist.

**Complexity:**  
- Time: O(n)  
- Space: O(n)

---
