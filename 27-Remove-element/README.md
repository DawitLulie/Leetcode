<h2><a href="https://leetcode.com/problems/remove-element">Remove Element</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences of <code>val</code> in <code>nums</code> in-place. The order of the elements may be changed. Then return the number of elements in <code>nums</code> which are not equal to <code>val</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return length = 2, with the first two elements of nums being 2. It doesn't matter what you leave beyond the returned length.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return length = 5, with the first five elements of nums being 0, 1, 4, 0, and 3. Note that the order of the elements can be changed. It doesn't matter what you leave beyond the returned length.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>0 <= nums.length <= 100</code></li>
  <li><code>0 <= nums[i] <= 50</code></li>
  <li><code>0 <= val <= 100</code></li>
</ul>

---

### Solution

**Approach:**  
We use a two-pointer technique to solve this problem in-place. The idea is to maintain a pointer <code>i</code> that tracks the position where the next non-<code>val</code> element should be placed. As we iterate through the array:
- If the current element is not equal to <code>val</code>, we place it at position <code>i</code> and increment <code>i</code>.
- If the current element is equal to <code>val</code>, we simply skip it.

At the end of the iteration, <code>i</code> will represent the number of elements that are not equal to <code>val</code>, and the first <code>i</code> elements in <code>nums</code> will be the desired elements.

**Time Complexity:**  
- O(n), where n is the length of the array. We traverse the array exactly once.

**Space Complexity:**  
- O(1), as we are modifying the array in-place without using any extra space.
