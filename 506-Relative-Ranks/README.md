<h2><a href="https://leetcode.com/problems/relative-ranks">506. Relative Ranks</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given an integer array <code>score</code> of athletes.  
Return an array <code>answer</code> where <code>answer[i]</code> is the rank of the <code>i</code>-th athlete.</p>

<p>The ranking rules are:</p>
<ul>
  <li>The top 3 highest scores get "Gold Medal", "Silver Medal", and "Bronze Medal".</li>
  <li>The rest receive their numeric rank starting from 4 as a string.</li>
</ul>

<p><strong>Example 1:</strong></p>
<pre>
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 &lt;= score.length &lt;= 10<sup>4</sup></code></li>
  <li><code>0 &lt;= score[i] &lt;= 10<sup>6</sup></code></li>
  <li>All scores are unique.</li>
</ul>

---

### Solution

**Approach:**  
Sort the scores in descending order.  
Assign "Gold Medal", "Silver Medal", "Bronze Medal" for top 3.  
For others, assign their numeric rank as a string.  
Map ranks back to the original order.

**Complexity:**  
- Time: O(n log n)  
- Space: O(n)

---
