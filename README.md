# Competitive Programming

Crucial information that is necessary to ace programming interviews.

This repository also consists of possible questions asked in interviews with FAANG companies and their solutions.

Language: Python

Author: Arkaan Quanunga

# Big O(n)

When writing algorithms, we must always consider 3 things.

1. Readability of Code - Depending on the team you are working with, you should consider the readability
of your code. Some teams can understand complex algorithms and some can't. Work around your team to build the knowledge
from bottom- up. 
2. Time complexity- As the size of input increases, the time taken for giving a solution is always a consideration. You want
to minimise the time taken for giving a solution. Usually it is through using more space or thinking of a better logic.
3. Space complexity - How much memory is consumed, when providing the solution.




# Data Structures

Understanding different data structures is the key to write
optimised algorithms. 

## Arrays

Example: [1,2,3,4,5]


## Hash Maps

Example: {a:1, b:2, c: 3, d: 7}


## Strings

Example: "abc"

### Substrings

Example: 

### Palindrome

Example: "racecar" reversed is "racecar"

## Linked Lists


### Singly Linked List

`class ListNode{
        value: any,
        next: ListNode
}
` 

Example: 1 => 2 => 3 => 4 => 5 => None

1 = Head
5 = Tail

### Doubly Linked List

`class ListNode{
        value: any,
        prev: ListNode,
        next: ListNode
}
`

Example: None <= 1 <=> 2 <=> 3 <=> 4 <=> 5 => None

1 = Head
5 = Tail

### Multi Level Doubly Linked List

[See here for visualisation](flattenMultiLevelDoublyLinkedList.py)


### Cycle detection


# Stacks 

Limiting the number of operations that can be done on a particular data structure is helpful with performance.

Last In First out (LIFO)

Look up: O(n)

pop: O(1)

push: O(1)

peek: O(1)

Example: Browsing History
        
1. Google
2. udemy.com
3. youtube


1. youtube
2. udemy
3. Google



## Can build with:
1. Arrays 
2. Linked Lists

This depends on the functions you want to perform on a stack.

Arrays have Cache locality => faster when accessing items as in memory they are next to each other.
Can be dynamic array or static array. When converting from static to dynamic, it needs to double memory to increase the memory. 

Linked Lists have extra memory for the pointers and have more dynamic memory than arrays.


# Queues

First In First Out (FIFO)

Look up: O(n)

enqueue: O(1)

dequeue: O(1)

peek: O(1)

Example: 

People queueing for restaurant or roller coaster ride

Matt -- Joy -- Samir -- Pavel 

1. Matt
2. Joy
3. Samir
4. Pavel


## Can build with:

1. Arrays
2. Linked Lists => Much better to use for Queues

Don't every build queue with arrays. 
Arrays have indexes associated to them. So as u remove the first item, all the indexes needs to shift.
O(N) operation

O(1) operations for linked list while changing the head and the tail in linked list.

### Advantages of Stacks & Queues

1. Fast Operations
2. Fast peek
3. Ordered

### Disadvantages of Stacks & Queues

1. Slow Lookup



