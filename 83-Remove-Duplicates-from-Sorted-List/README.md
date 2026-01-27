<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list">Remove Duplicates from Sorted List</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given the <code>head</code> of a sorted linked list, delete all duplicates such that each element appears only once.</p>

<p>Return the linked list sorted as well.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: head = [1,1,2]
Output: [1,2]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: head = [1,1,2,3,3]
Output: [1,2,3]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>The number of nodes in the list is in the range [0, 300]</li>
  <li>-100 &lt;= Node.val &lt;= 100</li>
  <li>The list is guaranteed to be sorted in ascending order.</li>
</ul>

---

### Solution

<strong>Approach:</strong>  
Traverse the list once.  
If the current node value is the same as the next node value, skip the next node.  
Otherwise, move forward.

<strong>Complexity:</strong>  
- Time: O(n)  
- Space: O(1)

---
