# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 20:44:14 2020
week01 assignment
@author: Zhu Yuting
"""


# 26. Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        nums.sort()
        
        #check empty array
        if not nums:
            return 0
        
        #initialization
        counter = 1
        
        # if the next element is not equal to the current one ,add in the array
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i]:
                nums[counter] = nums[i+1]
                counter +=1
                
        return counter
                
    
# 189. Rotate Array
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        k = k % len(nums)

        if k == 0:
        	return

        while k > 0:
            p = nums[-1]
            nums.pop()
            nums.insert(0, p)
            k -= 1
        return
    
    
    
    
    
 #21. Merge Two Sorted Lists   
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        first = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 or l2
        return first.next
    

# 88. Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        while m > 0 and  n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -=1
        if n > 0:
            nums1[:n] = nums2[:n]
 

#1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

# 283. Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index +=1
        for j in range(index,len(nums)):
            nums[j] = 0
        
# 66. Plus One
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == []:
            return [1]
        if digits[-1] != 9:
            return digits[:-1]+[digits[-1]+1]
        else:
            return self.plusOne(digits[:-1])+[0]

# 641. Design Circular Deque (Medium)
 


# 42. Trapping Rain Water (Hard)
def trap(self, bars):
    if not bars or len(bars) < 3:
        return 0
    volume = 0
    left, right = 0, len(bars) - 1
    l_max, r_max = bars[left], bars[right]
    while left < right:
        l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
        if l_max <= r_max:
            volume += l_max - bars[left]
            left += 1
        else:
            volume += r_max - bars[right]
            right -= 1
    return volume


