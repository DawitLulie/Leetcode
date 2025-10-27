<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii">Best Time to Buy and Sell Stock II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times), but you must sell the stock before you buy again. Return the maximum profit you can achieve.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1), sell on day 3 (price = 5), profit = 4.
Then buy on day 4 (price = 3), sell on day 5 (price = 6), profit = 3.
Total profit = 4 + 3 = 7.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1, sell on day 5, profit = 4.
</pre>

<p><strong>Example 3:</strong></p>
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
Iterate through the array:
1. Whenever the current price is higher than the previous day, buy at previous day and sell at current day.  
2. Add the profit to the total profit.  
3. Continue for the entire array.  

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
