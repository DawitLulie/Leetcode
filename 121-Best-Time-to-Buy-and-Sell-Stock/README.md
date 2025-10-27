<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock">Best Time to Buy and Sell Stock</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No transactions are done, max profit = 0.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= prices.length &lt;= 10<sup>5</sup></li>
  <li>0 &lt;= prices[i] &lt;= 10<sup>4</sup></li>
</ul>

---

### Solution

**Approach:**  
Iterate through the prices array:
1. Track the **minimum price** seen so far.  
2. For each price, calculate potential profit if sold at this price.  
3. Update the **maximum profit** accordingly.  
4. Return the maximum profit found.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
