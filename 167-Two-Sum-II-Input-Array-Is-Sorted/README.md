<h2><a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted">Two Sum II - Input Array Is Sorted</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a **1-indexed** array of integers <code>numbers</code> that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be <code>numbers[index1]</code> and <code>numbers[index2]</code> where 1 &lt;= index1 &lt; index2 &lt;= numbers.length.</p>

<p>Return the indices of the two numbers, <strong>1-indexed</strong>, as an integer array <code>[index1, index2]</code> of length 2.</p>

<p>You may assume that each input would have exactly one solution and you may not use the same element twice.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: 2 + 7 = 9
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: numbers = [2,3,4], target = 6
Output: [1,3]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>2 &lt;= numbers.length &lt;= 3 * 10<sup>4</sup></li>
  <li>-1000 &lt;= numbers[i] &lt;= 1000</li>
  <li>numbers is sorted in non-decreasing order.</li>
  <li>-1000 &lt;= target &lt;= 1000</li>
  <li>Only one valid answer exists.</li>
</ul>

---

### Solution

**Approach:**  
1. Use two pointers, `left` at start and `right` at end.  
2. Calculate `sum = numbers[left] + numbers[right]`.  
3. If `sum == target`, return 1-indexed positions.  
4. If `sum < target`, move `left` forward.  
5. If `sum > target`, move `right` backward.  
6. Continue until the pair is found.  

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
