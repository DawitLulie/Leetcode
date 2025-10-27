<h2><a href="https://leetcode.com/problems/repeated-dna-sequences">Repeated DNA Sequences</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>The DNA sequence is composed of a series of nucleotides: 'A', 'C', 'G', and 'T'. Given a string <code>s</code> that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>0 &lt;= s.length &lt;= 10<sup>5</sup></li>
  <li><code>s[i]</code> is 'A', 'C', 'G', or 'T'.</li>
</ul>

---

### Solution

**Approach:**  
1. Use a sliding window of length 10.  
2. Store each 10-letter sequence in a `seen` set.  
3. If a sequence is already in `seen`, add it to the `repeated` set.  
4. Return the list of repeated sequences.  

**Time Complexity:** O(n)  
**Space Complexity:** O(n)
