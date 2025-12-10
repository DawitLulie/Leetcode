<h2><a href="https://leetcode.com/problems/longest-harmonious-subsequence">594. Longest Harmonious Subsequence</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />
<hr>

<p>We define a harmonious array as an array where the difference between its maximum and minimum values is exactly <code>1</code>.</p>

<p>Given an integer array <code>nums</code>, return the length of the longest harmonious subsequence among all possible subsequences of <code>nums</code>.</p>

<p><strong>A subsequence</strong> of an array is a sequence that can be derived from the original array by deleting some or no elements without changing the order of the remaining elements.</p>

---

### Example 1:
<pre>
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
</pre>

### Example 2:
<pre>
Input: nums = [1,2,3,4]
Output: 2
</pre>

### Example 3:
<pre>
Input: nums = [1,1,1,1]
Output: 0
</pre>

---

### Constraints:
<ul>
  <li>1 ≤ nums.length ≤ 2 × 10<sup>4</sup></li>
  <li>-10<sup>9</sup> ≤ nums[i] ≤ 10<sup>9</sup></li>
</ul>

---

### Solution

**Approach:**  
Count how many times each number appears using a dictionary.  
Then, for each number, check if the next consecutive number exists, and update the longest length.

---

### Complexity

- ⏱ **Time Complexity:** O(n)  
- 💾 **Space Complexity:** O(n)

---

### Performance (LeetSync)

> **Time:** 108 ms (77.45%)  
> **Memory:** 18.1 MB (18.70%)

---
