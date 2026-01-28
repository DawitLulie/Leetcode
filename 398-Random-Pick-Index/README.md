<h2>
  <a href="https://leetcode.com/problems/random-pick-index">
    Random Pick Index
  </a>
</h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty: Medium" />
<hr>

<p>
Given an integer array <code>nums</code> with possible duplicates, write a class to pick a random index of a given target number.  
Each target number must have the <strong>same probability</strong> of being chosen.
</p>

<p>
Implement the <code>Solution</code> class:
</p>

<ul>
  <li><code>Solution(vector&lt;int&gt;& nums)</code> Initializes the object with the array <code>nums</code>.</li>
  <li><code>int pick(int target)</code> Returns a random index <code>i</code> such that <code>nums[i] == target</code>.</li>
</ul>

<p><strong>Example:</strong></p>

<pre>
Input
["Solution", "pick", "pick", "pick"]
[[[1,2,3,3,3]], [3], [1], [3]]

Output
[null, 4, 0, 2]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ nums.length ≤ 2 * 10⁴</li>
  <li>-2³¹ ≤ nums[i] ≤ 2³¹ - 1</li>
  <li>target exists in nums</li>
  <li>At most 10⁴ calls will be made to pick</li>
</ul>

---

### Solution

**Approach:**  
- Store all indices for each number in a map.  
- To pick a target, randomly select one index from the list.  

**Complexity:**  
- Time: O(n) for initialization, O(1) per pick  
- Space: O(n)  

---
