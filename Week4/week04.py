# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:23:16 2020

Week 04 assignment
@author: zhuyuting
"""
# 860. Lemonade Change
class Solution(object): #aw
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
    
    
# 455. Assign Cookies Greedy algorithm
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        #two pointer
        IndexG = 0;
        IndexS = 0;
        
        while (IndexG < len(g) and IndexS < len(s)):
            if g[IndexG] <= s[IndexS]:
                IndexG += 1
                IndexS += 1
            else:
                IndexS += 1
        return IndexG
 # 时间复杂度：O(nlogn+mlogm)O(nlogn+mlogm)，n 是 g.length，m 是 s.length，排序的时间。空间复杂度：O(1)
 
 # 122. Best Time to Buy and Sell Stock II