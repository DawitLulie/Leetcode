<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii">Remove Duplicates from Sorted List II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given the <code>head</code> of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.</p>

<p>Return the linked list sorted as well.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: head = [1,1,1,2,3]
Output: [2,3]
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
Use a dummy node to handle edge cases.  
Traverse the list and skip all values that appear more than once.  
Only link nodes with unique values.

<strong>Complexity:</strong>  
- Time: O(n)  
- Space: O(1)

---
