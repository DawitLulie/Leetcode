<h2><a href="https://leetcode.com/problems/top-k-frequent-elements">Top K Frequent Elements</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the <code>k</code> most frequent elements.</p>

<p>You may return the answer in <strong>any order</strong>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1], k = 1
Output: [1]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 10<sup>5</sup></li>
  <li>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></li>
  <li><code>k</code> is in the range <code>[1, unique elements in nums]</code></li>
</ul>

<p><strong>Follow-up:</strong> Can you solve it in <code>O(n)</code> time?</p>

---

### Solution

**Approach:**  
Count frequencies using a dictionary.  
Use a bucket list where index = frequency.  
Iterate buckets from high to low until you collect k elements.

**Complexity:**  
- Time: O(n)  
- Space: O(n)
