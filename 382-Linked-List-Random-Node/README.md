<h2>
  <a href="https://leetcode.com/problems/linked-list-random-node">
    Linked List Random Node
  </a>
</h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty: Medium" />
<hr>

<p>
Given a singly linked list, return a random node's value from the linked list.
Each node must have the <strong>same probability</strong> of being chosen.
</p>

<p>
Implement the <code>Solution</code> class:
</p>

<ul>
  <li><code>Solution(ListNode* head)</code> initializes the object with the head of the list.</li>
  <li><code>int getRandom()</code> returns a random node's value.</li>
</ul>

<p><strong>Example:</strong></p>

<pre>
Input
["Solution", "getRandom", "getRandom", "getRandom"]
[[[1,2,3]], [], [], []]

Output
[null, 1, 3, 2]
</pre>

<p>
Each element should have equal probability of being returned.
</p>

<p><strong>Constraints:</strong></p>
<ul>
  <li>The number of nodes is between 1 and 10<sup>4</sup></li>
  <li>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></li>
</ul>

---

### Solution

<strong>Approach:</strong><br>
Store all node values in a vector during initialization.  
Pick a random index each time <code>getRandom()</code> is called.

<strong>Complexity:</strong>
<ul>
  <li>Time: O(n) for initialization, O(1) per query</li>
  <li>Space: O(n)</li>
</ul>

---
