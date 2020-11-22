学习笔记
1.Python中定义数组与链表的方式
```python
# Make a list
Lists = ['I','love','study','data','science']
# Male a list node
class Node(object):
#节点类
    #功能：输入一个值data，将值变为一个节点
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return self.data
```
2.三数之和
(1)暴力求解 O(n^3); 
(2)哈希表 O(N^2); 
(3)排序后双指针夹逼 O(N^2)→固定指针复杂度: O(N) * O(N)双指针i,j的复杂度

3.链表实战题目不熟练需要多加练习
重点环形链表 