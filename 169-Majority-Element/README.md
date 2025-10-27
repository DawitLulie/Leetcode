<h2><a href="https://leetcode.com/problems/majority-element">Majority Element</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an array <code>nums</code> of size <code>n</code>, return the majority element. The majority element is the element that appears **more than ⌊n / 2⌋ times**.</p>

<p>You may assume that the majority element always exists in the array.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [3,2,3]
Output: 3
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [2,2,1,1,1,2,2]
Output: 2
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>n == nums.length</li>
  <li>1 &lt;= n &lt;= 5 * 10<sup>4</sup></li>
  <li>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></li>
</ul>

---

### Solution

**Approach:**  
1. Use a dictionary to count the frequency of each number.  
2. For each number, increment its count.  
3. Return the number as soon as its count exceeds half of the array size.  

**Time Complexity:** O(n)  
**Space Complexity:** O(n)
