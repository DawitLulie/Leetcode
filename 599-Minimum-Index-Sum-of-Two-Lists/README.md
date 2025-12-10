<h2><a href="https://leetcode.com/problems/minimum-index-sum-of-two-lists">599. Minimum Index Sum of Two Lists</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />
<hr>

<p>Given two string arrays <code>list1</code> and <code>list2</code>, find the common strings with the **least sum of their indices**.</p>

<p>Return all such strings in **any order**.</p>

---

### Example 1:
<pre>
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
       list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: "Shogun" is the only common string with index sum 0 + 3 = 3.
</pre>

### Example 2:
<pre>
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
       list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: Index sums are: "Shogun" 0+1=1, "KFC" 3+0=3, "Burger King" 2+2=4. Minimum is 1.
</pre>

---

### Constraints:
<ul>
  <li>1 ≤ list1.length, list2.length ≤ 1000</li>
  <li>1 ≤ list1[i].length, list2[i].length ≤ 30</li>
  <li>All strings are unique within each list</li>
</ul>

---

### Solution

**Approach:**  
Use a dictionary to store the indices of `list1`.  
Iterate `list2`, check if the string exists in `list1` and calculate the sum of indices.  
Keep track of the minimum sum and the corresponding strings.

---

### Performance (LeetSync)

⏱ Time: 92 ms (83.24%) | 💾 Memory: 14.5 MB (91.12%) - LeetSync
