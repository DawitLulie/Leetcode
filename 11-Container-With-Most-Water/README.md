<h2><a href="https://leetcode.com/problems/container-with-most-water">Container With Most Water</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an array <code>height</code> of length <code>n</>.  
There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p>Return <em>the maximum amount of water a container can store</em>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: height = [1,1]
Output: 1
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>n == height.length</code></li>
  <li><code>2 <= n <= 10^5</code></li>
  <li><code>0 <= height[i] <= 10^4</code></li>
</ul>

---

### Solution

**Approach:**  
Use two pointers, one at the start and one at the end of the array.  
At each step, calculate the container area and move the pointer pointing to the smaller height toward the other pointer.  
Keep track of the maximum area.

**Complexity:**  
- Time: <code>O(n)</code>  
- Space: <code>O(1)</code>
