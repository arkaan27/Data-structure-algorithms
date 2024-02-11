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

### Possible functions
1. lookup: O(1)
2. push: O(1)
3. insert: O(n)
4. delete: O(n)
5. unshift: O(n)
6. splice: O(n)

### Static arrays

[Juice, Apple, Cheese, Kale, Mango , Grapes]

### Dynamic Arrays:

da= []

da.append("Juice")


## Hash Maps

Example: {a:1, b:2, c: 3, d: 7}

### Hash Function

MD5 Hash: 5d41402avc4b2a76b9719d911017c592

Different strings will have different Hash

Indempotent- given the same input gives the same output

### Hash Functions & Collisions

1. Insert O(1)
2. lookup O(1)
3. delete O(1)
4. search O(1)

if Hash collisions happen then Big O notation becomes O(N)

To deal with this there are [Linked Lists](##Linked-Lists)


### Hash Tables vs Arrays
        Array           Hash Tables
        Search: O(N)    Search: O(1)
        lookup: O(1)    lookup: O(1)
        insert: O(n)    insert: O(1)
        delete: O(n)    delete: O(1)

All of the above is dependent if no hash collisions happen.


## Strings

Example: "abc"

### Substrings

Example: 

### Palindrome

Example: "racecar" reversed is "racecar"

##Linked Lists


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

[See here for visualisation](Linked_lists/flatten_multi_level_doubly_linked_list.py)


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



