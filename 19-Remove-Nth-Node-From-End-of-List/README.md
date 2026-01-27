<h2><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list">Remove Nth Node From End of List</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given the <code>head</code> of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: head = [1], n = 1
Output: []
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: head = [1,2], n = 1
Output: [1]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>The number of nodes in the list is sz.</li>
  <li>1 &lt;= sz &lt;= 30</li>
  <li>0 &lt;= Node.val &lt;= 100</li>
  <li>1 &lt;= n &lt;= sz</li>
</ul>

---

### Solution

<strong>Approach:</strong>  
Use two pointers.  
Move the first pointer <code>n</code> steps ahead.  
Then move both pointers together until the first reaches the end.  
Remove the target node.

<strong>Complexity:</strong>  
- Time: O(n)  
- Space: O(1)

---
