<h2><a href="https://leetcode.com/problems/median-of-two-sorted-arrays">Median of Two Sorted Arrays</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <em>the median of the two sorted arrays</em>.</p>

<p>You must solve the problem in <strong>O(log (m+n))</strong> time complexity.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>nums1.length == m</code></li>
  <li><code>nums2.length == n</code></li>
  <li><code>0 <= m, n <= 1000</code></li>
  <li><code>1 <= m + n <= 2000</code></li>
  <li><code>-10<sup>6</sup> <= nums1[i], nums2[i] <= 10<sup>6</sup></code></li>
</ul>

---

### Solution

**Approach:**  
Combine both input arrays into a single array and sort it.  
Then check if the total length is odd or even:

- If odd → return the middle value.
- If even → return the average of the two middle values.

This approach is simple and easy to implement, but it does not meet the required time complexity from the follow-up.

**Complexity:**  
- Time: <code>O((m+n) log (m+n))</code> due to sorting  
- Space: <code>O(m+n)</code>
