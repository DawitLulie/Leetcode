<h2><a href="https://leetcode.com/problems/min-stack">Min Stack</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.</p>

<p>Implement the <code>MinStack</code> class:</p>
<ul>
  <li><code>MinStack()</code> initializes the stack.</li>
  <li><code>void push(int val)</code> pushes the element <code>val</code> onto the stack.</li>
  <li><code>void pop()</code> removes the element on the top of the stack.</li>
  <li><code>int top()</code> gets the top element of the stack.</li>
  <li><code>int getMin()</code> retrieves the minimum element in the stack.</li>
</ul>

<p><strong>Example 1:</strong></p>
<pre>
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</li>
  <li>Methods <code>pop</code>, <code>top</code>, and <code>getMin</code> will always be called on non-empty stacks.</li>
  <li>At most 3 * 10<sup>4</sup> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, and <code>getMin</code>.</li>
</ul>

---

### Solution

**Approach:**  
Use two stacks:
1. `st` stores all the values.  
2. `minSt` keeps track of the minimum values.  
- Push: Add to `st` and update `minSt` if necessary.  
- Pop: Remove from `st` and `minSt` if the top was the minimum.  
- Top: Return `st.top()`.  
- getMin: Return `minSt.top()`.  

**Time Complexity:** O(1) per operation  
**Space Complexity:** O(n)
