#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:37:27 2018

@author: Diana Ramirez 88604827
Professor: Diego Aguire
Class: CS 2302 TR 1:30PM
Lab 2A
"""
from Node import Node

class linkedList(object):
    
    def __init__(self, head = None):
        self.head = head
        
       
    def addNew(self,int):
        newNode = Node(int)
        if self.head == None:
            self.head = newNode
        else:    
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode    
        
    def lengthlist(self):
        temp = self.head
        length = 0
        while(temp.next != None):
            length+=1
            temp = temp.next
        return length            
    
    def printList(self):
        print("Printing linked list.....")
        if(self.head is None):
            return;
        temp = self.head
        while(temp!= None):
            print(temp.item,",",end =" ")
            temp = temp.next
        print()    
    def copy(self):
        final = linkedList()
        curr = self.head
        while curr != None:
            final.addNew(curr.item)
            curr = curr.next
        return final   
        
            
   #####################solution 1, nested loops ####################
    def nestedLoops(self): 
        nodeCompare = self.head
        while(nodeCompare != None):
            curr = nodeCompare.next
            while(curr != None):
                if(nodeCompare.item == curr.item):
                    print("Number",curr.item,"is repeated",",",end =" ")
                curr = curr.next
            nodeCompare = nodeCompare.next
            
    #############solution 2 : bubbleSort method for the list##############           
    def bubbleSort(self):
        swaps=0
        if(self.head == None):
            print("No nodes to sort, list is empty")
        elif self.head.next == None:
            return self.head
        else:
            temp = self.head
            while temp.next != None:
                curr = temp.next
                while curr.next != None:
                    if temp.item > curr.item:
                        ##where the swapping of data occurs
                        dummy = temp.item
                        temp.item = curr.item
                        curr.item = dummy
                        swaps+=1
                    curr = curr.next
                temp = temp.next 
            print("Number of swaps", swaps)
                    
#########################solution 3: merge Sort##########################
##actual mergeSort method that calls the middle() and mergeLists() methods recursively
##this is outside of the linked list class
def mergeSort(head):
    if (head == None or head.next == None):
        return head
        
    left, right = middle(head)
    left = mergeSort(left)
    right = mergeSort(right)
        
    head = merge(left,right)
    
    return head   
##method to unite both halfs of the list
def merge(left,right):
    temp = None
    if left == None:
        return right
    if right == None:
        return left
    if left.item <= right.item:
        temp = left
        temp.next = merge(left.next,right)
    else:
        temp = right
        temp.next = merge(left,right.next)
    return temp
##method used to cut the lists into 2                     
def middle(head):
    slow = head ##decides middle of list
    fast = head ##goes all the way to the end of list
    if fast:    
        fast = fast.next ##used to incremeten fast twice as much as slow
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
                
    mid = slow.next
    slow.next = None
    return head, mid    
###############################solution 4#####################################
def searchRepeat(listArray,repeatArray):
    ##seen is a boolean array that stores if values are repeated in list
    seen = [] 
    ##searching in list array
    for x in range (len(listArray)):
        y = listArray[x]
        ##if number in listArray is found in repeatArray add True to seen
        if y in repeatArray:
            seen.append(True)
        ##number not found in repeatArray so add false
        else:
            seen.append(False)
    print("Numbers seen: ")        
    print(seen)
    return seen       
       
             
def isRepeated(list):
    repeatArray = []
    listArray = []
    curr = list
    nodeCompare = list
    while(nodeCompare != None):
            curr = nodeCompare.next
            while(curr != None):
                ##if statement used to create repeatArray
                if(nodeCompare.item == curr.item and curr.item not in listArray):
                    ##creating an array of repeated numbers in the list
                    repeatArray.append(curr.item)
                curr = curr.next
            ##storing the elements of the list in an array    
            listArray.append(nodeCompare.item)    
            nodeCompare = nodeCompare.next
    ##calling method to create boolean array 
    searchRepeat(listArray,repeatArray)
        
    
##############################################################################    
    
##opening the files
activision = open('activision.txt')
vivendi = open('vivendi.txt')
##initializing the linkedList
ids_list = linkedList()

##separates and reads lines of file
linesActi = activision.readlines()
linesVive = vivendi.readlines()

##adds numbers in Activision file to the ids list
for ln in linesActi:
    ln = int(ln)
    ##using the LinkedList class
    ids_list.addNew(ln)
##adds numbers in Vivendi file to the ids list  
for ln2 in linesVive:
    ln2 = int(ln2)
    ##using the LinkedList class
    ids_list.addNew(ln2)
    
##making a copy of the unsorted list    
copy = ids_list.copy()

#####################solution 1######################
ids_list.nestedLoops()

######################solution 2#######################

ids_list.bubbleSort()
ids_list.printList()

######################solution 3########################
print("Merge sorted list:")
    ##returns nodes not a list, saved in node ids
ids  = mergeSort(ids_list.head)
    ##printing the sorted nodes
dummy = ids

while(dummy.next != None):
    print(dummy.item,",",end =" ")
    dummy = dummy.next
print()

######################solution 4#########################
copy.printList()
    ###used the unsorted copy of the original list
isRepeated(copy.head)

    

    
    