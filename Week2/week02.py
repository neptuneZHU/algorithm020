# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:19:18 2020
Week02 assignment
@author: zhuyuting

"""
# 242. Valid Anagram (Easy) Python using the dic to realize the hash table function

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #initialization of dic in python, using {} not []
        
        dic = {}
        
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
                
        for k in dic:
            if dic[k] != 0:
                return False
        
        return True
  
# 49. Group Anagrams (Medium)

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
# for each strs[i], need to compare the dic content

        strsmap = {}
        result = []
        
        for string in strs:
            tmp = ''.join(sorted(string))
            if tmp in strsmap:
                strsmap[tmp].append(string)
            else:
                strsmap[tmp] = [string]
                
        for str_list in strsmap.values():
            result.append(str_list)
            
        return result
            
    
    