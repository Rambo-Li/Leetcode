My solution to leetcode problems as well as my thought on them.

The order of the subjects is from https://neetcode.io/roadmap. 

I think coding comprises of three steps：
1. Nail down the minimal information needed. 
    What value to determine the result? Can you name it in English? How many pointers and values do you need?
2. Decide the data form in memory, it can be thought as data structure.
    The data hold in memory serves as the basis for computation. Manipulating them should be as easy as possible.
3. Decide the update rule, such as reading, adding, deleting, etc.
    How to manipulate the data? How to classify the scenarios so the code is easy to write and clean?  

Number representiveness is the fundation of computer programming. A number can represent two types of information, a value or a address(pointer, index). Complexity is when to increment/decrement it. When you have multiple numbers, they are connected through pointer operations, the complexity comes from when to add/remove/read it.

Discussion on the type of problems.
1. Array and hashing.
    --- pointer and value
    The pointer updates in a one-to-next looping fashion. The complexity can come from the semantics of index an d value, or interchanging them. 
    When the value decides the index(contrast to normal array), it becomes hashing table.
2. Two pointers.
    --- two pointers
    Pointer makes use of some operation to get the next value, no matter array or linked list. In array, it's i=i+1, in linked list, it's pointer=node.next. The is the iterator concept in most programming languages. The complexity comes from multiple pointers, their direction, speed, interaction, etc.
3. Stack.
    --- values stored by some criteria, and read from end or ends
    The main idea of stack is to hold the value first, then as the future data shows up, put some operation on the value. The value only come and go from the ends of the data structure, of course, the adding and popping rules can be complex. Stack can be used to update former values if later a bigger/smaller value comes up, so that you know what is the max/min after certain value.
4. Binary Search.
    --- two pointers, one mid pointer/value, one target value, one of the pointers can 'jump'
    Array index can 'jump' if the underlying value is ordered, instead of looping. This is the concept of binary search. The jump gives a narrower scope. The complexity can come from the searching scope, jumping conditions, classifying scenarios. Also, binary search has a recursive nature, which means a big problem's solving relies on same type, but smaller problems.
    Binary search space can be not just the obvious array, but also a [1, n] abstract space. You just need to define the update rule.
5. Sliding windows.
    --- two pointers with width.
    Complextity comes from update rules for pointers or width, or the interaction between them, the width of window may or may not change. 
6. Linked lists.
    --- multiple pointers.
    Pointers are the only way to access nodes. If pointers need to be changed, set up another pointer to hold the next node. To get any node in the linked list, you can 
    use multiple pointers going at different speed or start point.
7. Trees.
    --- one pointer with stack or queue
    Next operation is not enough for tree element traversal, so you need a stack or queue to hold the branches. Because of the unknown depth of either side, recursion sometimes is the only choice.