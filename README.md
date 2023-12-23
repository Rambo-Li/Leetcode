My solution to leetcode problems as well as my thought on them. New ideas are added as I develop them.

The order of the subjects and the problems are from https://neetcode.io/roadmap. 

I think coding comprises of three steps：
1. Find the information flow needed to solve the problem. 
    How to go from given information to answer? What is the minimal information you need to feed to the next step? What is the underlying structure of the flow? 
2. Decide the data form in memory, it can be thought as data structure.
    The data hold in memory serves as the basis for computation. Usually the usage pattern decides the data structure.
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
    --- one pointer with stack or queue, recursion.
    Next operation is not enough for tree element traversal, so you need a stack or queue to hold the branches. Recursion is a bit hard to think, but basically any problem that rely on small subproblem and small subproblem is easy can be written in recursion form. If there are unknown depth evolved, recursion is mostly the only choice.  Stack usually put all children on it, but you can vary like putting all left children on it then pop and do it again, which is how to traverse BST in value-order.
8. Trie.
    --- just like trees with alphabet braching.
9. Backtracking.
    --- recursion and you need to do something to the recursion result to get the answer. 
    There are two ways to build up the answer, one is go down to leaves and let the leaves return. The other way is start building result while you go down the tree. This method is the only choice if child needs all parents' information to build results. The branching is created by a for loop + recursive call. When dealing with duplicates, the best way is to avoid duplicates recursions from the first place, if this can't be done, try to use set, the last choice is use sorted array to avoid duplicates. 
    The word backtracking means using global variables so that each recursion modifies on the same data, instead of passing parameters to recursive call. If there is much informatin to be communicated between recursive calls, this is a better choice.
10. 1-D DP
    --- recursion based on several base cases. Or think of an array that latter elements build on former elements.
11. Heap and priority queue.
    --- BST root represents the mid(l < root < r), while heap root represents the min or max(l / r < root). 
12. Graph.
    --- in addition to the pointer and stack/queue for tree traversals, graph needs another data structure to hold the visited elements.
    The complexity comes from starting point/s, which nodes to put on the queue, and how to represent the visited set.
13. Intervals.
    --- two values
    If you sort the intervals, then only the right end matters.