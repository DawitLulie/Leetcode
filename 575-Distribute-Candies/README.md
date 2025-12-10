<h2><a href="https://leetcode.com/problems/distribute-candies">Distribute Candies</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Alice has <strong>n</strong> candies, where <code>n</code> is even. The candies are represented by an integer array <code>candyType</code>, where each value represents a type of candy.</p>

<p>Alice must give <strong>exactly n / 2</strong> candies to her sister. Return the <strong>maximum number of different candy types</strong> Alice can give to her sister.</p>

---

### Example 1:
<pre>
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: She can give one each of (1,2,3).
</pre>

### Example 2:
<pre>
Input: candyType = [1,1,2,3]
Output: 2
</pre>

### Example 3:
<pre>
Input: candyType = [6,6,6,6]
Output: 1
</pre>

---

### Constraints:
<ul>
  <li>2 <= candyType.length <= 10<sup>4</sup></li>
  <li>candyType.length is even</li>
  <li>-10<sup>5</sup> <= candyType[i] <= 10<sup>5</sup></li>
</ul>

---

### Solution

**Approach:**  
Count how many unique candy types exist.  
Alice can only take `n/2` candies, so the answer is the minimum of:

- number of unique candy types  
- n / 2  

---

**Complexity:**  
- Time: **O(n)**  
- Space: **O(n)**

---
