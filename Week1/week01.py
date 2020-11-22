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

#622. Design Circular Queue
class Node:
    def __init__(self,value):
        self.val = value
        self.next = self.pre = None
       
class CircularQueue:
    def __init__(self,k):
        self.size = k
        self.curSize = 0
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def enqueue(self,value):
        if self.curSize < self.size:
            node = Node(value)
            node.pre = self.tail.pre
            node.next = self.tail
            node.pre.next = node.next.pre = node
            self.curSize +=1
            return True
        return False
    
    def dequeue(self):
        if self.curSize > 0:
            node = self.head.next
            node.pre.next = node.next
            node.next.pre = node.pre
            self.curSize -=1
            return True
        return False
    
    def Front(self):
        return self.head.next.val
    
    def Rear(self):
        return self.tail.pre.val
    
    def isEmpty(self):
        return self.curSize == 0
    
    def isFull(self):
        return self.curSize == self.size
        

# 641. Design Circular Deque (Medium)
class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None
        
class MyCircularDeque:

    def __init__(self, k):
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = k
        self.curSize = 0

    def add(self, value, preNode):
        new = Node(value)
        new.pre = preNode
        new.next = preNode.next
        new.pre.next = new.next.pre = new
        self.curSize += 1
        
    def remove(self, preNode):
        node = preNode.next
        node.pre.next = node.next
        node.next.pre = node.pre
        self.curSize -= 1
    
    def insertFront(self, value):
        if self.curSize < self.size:
            self.add(value, self.head)
            return True
        return False

    def insertLast(self, value):
        if self.curSize < self.size:
            self.add(value, self.tail.pre)
            return True
        return False

    def deleteFront(self):
        if self.curSize:
            self.remove(self.head)
            return True
        return False

    def deleteLast(self):
        if self.curSize:
            self.remove(self.tail.pre.pre)
            return True
        return False

    def getFront(self):
        if self.curSize:
            return self.head.next.val
        return -1

    def getRear(self):
        if self.curSize:
            return self.tail.pre.val
        return -1

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size


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


