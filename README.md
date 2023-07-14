My solution to leetcode problems as well as my thought on them.

The order of the subjects is from https://neetcode.io/roadmap. 

I think coding comprises of three steps：
1. Nail down the minimal information needed. 
    What value to determine the result? Can you name it in English?
2. Decide the data form in memory, it can be thought as data structure.
    The data hold in memory serves as the basis for computation. Manipulating them should be as easy as possible.
3. Decide the update rule, such as reading, adding, deleting, etc.
    How to manipulate the data? How to classify the scenarios so the code is easy to write and clean?  

Number representiveness is the fundation of computer programming. A number can represent two types of information, a value or a address(pointer, index).

Discussion on the type of problems.
1. Array and hashing.
    --- pointer and value
    The fastest way of reading a data is to use an index. This is a O(1) operation. This is what array offers. The complexity can come from the semantics of index an d value, or interchanging them. 
    When the value decides the index(contrast to normal array), it becomes hashing table.
2. Two pointers.
    --- two pointers
    Pointer makes use of some operation to get the next value, no matter array or linked list. In array, it's i=i+1, in linked list, it's pointer=node.next. The is the iterator concept in most programming languages. The complexity comes from multiple pointers, their direction, speed, etc.
3. Stack.
    --- values, one pointer
    Another O(1) reading operation is to read from either end. The is the main idea of stack and queue. The value only come and go from the ends of the data structure, of course, the update rules can be complex.
4. Binary Search.
    --- two pointers, one mid pointer/value, one target value
    Array index can 'jump' if the underlying value is ordered, instead of looping. This is the concept of binary search. The jump gives a narrower scope. The complexity can come from the searching scope, jumping conditions, classifying scenarios. Also, binary search has a recursive nature, which means a big problem's solving relies on same type, but smaller problems and the easiest cases can be easily solved.
