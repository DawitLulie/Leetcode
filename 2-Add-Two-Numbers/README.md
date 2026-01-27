<h2><a href="https://leetcode.com/problems/add-two-numbers">Add Two Numbers</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given two <strong>non-empty linked lists</strong> representing two non-negative integers.</p>

<p>The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit.</p>

<p>Add the two numbers and return the sum as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: l1 = [0], l2 = [0]
Output: [0]
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>The number of nodes in each linked list is in the range [1, 100]</li>
  <li>0 &lt;= Node.val &lt;= 9</li>
  <li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>

---

### Solution

<strong>Approach:</strong>  
Traverse both linked lists at the same time.  
Add corresponding digits along with a carry.  
Create a new linked list to store the result.

<strong>Complexity:</strong>  
- Time: O(max(n, m))  
- Space: O(max(n, m))

---
