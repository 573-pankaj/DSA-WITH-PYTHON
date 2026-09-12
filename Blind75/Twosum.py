class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {} # Dictionary to store the numbers we have seen and their indices
        # print(seen)
        for i, num in enumerate(nums):

            complement = target - num
            # print(seen)
            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
            

solution = Solution()

answer = solution.twoSum([2, 7, 11, 15], 9)
print(answer)
            
# # ===============================
# """ 
# Yes. From now on, I’ll structure your **Python coding-problem solutions using classes and objects**, in the style used by platforms such as LeetCode.

# Your given template is essentially:

# ```python
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         # :type nums: List[int]
#         # :type target: int
#         # :rtype: List[int]
        


# The important concepts here are **class, object, method, `self`, parameters, and `return`**.

# ## 1. First understand the class structure

# ```python
# class Solution(object):
# ```

# This creates a class called `Solution`.

# Think of a class as a **blueprint**.

# ---

# ### The method

# ```python
# def twoSum(self, nums, target):
# ```

# `twoSum` is a **method** belonging to the `Solution` class.

# There are three things here:

# ```text
# self       → object itself
# nums       → input array
# target     → target value
# ```

# For example:

# ```python
# nums = [2, 7, 11, 15]
# target = 9
# ```

# The platform essentially uses the method with these inputs.

# ---

# # 2. What is `self`?

# This is important for upcoming problems.

# When we write:

# ```python
# class Solution(object):
#     def twoSum(self, nums, target):
# ```

# `self` represents the **current object of the class**.

# You don't normally pass `self` manually when calling the method.

# For example:

# ```python
# solution = Solution()

# answer = solution.twoSum([2, 7, 11, 15], 9)
# ```

# Python automatically passes:

# ```text
# solution → self
# [2,7,11,15] → nums
# 9 → target
# ```

# Conceptually:

# ```text
# # twoSum(self, nums, target)
# #    ↓       ↓      ↓
# #  object   array  target
# ```

# ---

# # 3. Solve Two Sum Using the Class

# Here is the complete solution:

# ```python
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         # :type nums: List[int]
#         # :type target: int
#         # :rtype: List[int]
#         """

#         seen = {}

#         for i, num in enumerate(nums):

#             complement = target - num

#             if complement in seen:
#                 return [seen[complement], i]

#             seen[num] = i
# ```

# This is the version you should submit to LeetCode.

# ---

# # 4. Understand the Code Step-by-Step

# ## Step 1: Create the class

# ```python
# class Solution(object):
# ```

# LeetCode expects a class named:

# ```text
# Solution
# ```

# ---

# ## Step 2: Create the method

# ```python
# def twoSum(self, nums, target):
# ```

# The method receives:

# ```text
# nums   → array
# target → required sum
# ```

# For example:

# ```text
# nums = [2,7,11,15]
# target = 9
# ```

# ---

# ## Step 3: Create dictionary

# ```python
# seen = {}
# ```

# We will store:

# ```text
# number → index
# ```

# Initially:

# ```text
# seen = {}
# ```

# ---

# ## Step 4: Iterate through the array

# ```python
# for i, num in enumerate(nums):
# ```

# For:

# ```python
# nums = [2, 7, 11, 15]
# ```

# we get:

# ```text
# i       num
# ────────────
# 0        2
# 1        7
# 2       11
# 3       15
# ```

# ---

# ## Step 5: Calculate complement

# ```python
# complement = target - num
# ```

# For the first element:

# ```text
# target = 9
# num = 2

# complement = 9 - 2
#             #  = 7


# So we need to find `7`.

# ---

# ## Step 6: Search dictionary

# ```python
# if complement in seen:
# ```

# We ask:

# > Have we already seen the number that we need?

# For the first `2`:

# ```text
# seen = {}
# 7 in seen?
# NO
# ```

# So store:

# ```python
# seen[num] = i
# ```

# which means:

# ```python
# seen[2] = 0
# ```

# Now:

# ```text
# seen = {
#     2: 0
# }
# ```

# ---

# ## Step 7: Second iteration

# Now:

# ```text
# i = 1
# num = 7
# ```

# Calculate:

# ```text
# complement = 9 - 7
#             = 2
# ```

# Check:

# ```python
# if 2 in seen:
# ```

# Yes!

# We have:

# ```python
# seen[2] = 0
# ```

# Current index:

# ```text
# i = 1
# ```

# Therefore:

# ```python
# return [seen[complement], i]
# ```

# becomes:

# ```python
# return [0, 1]
# ```

# ---

# # 5. What About the Comments?

# You wrote:

# python
# :type target: int
# :rtype: List[int]


# These are **type documentation comments** used by LeetCode.

# A more complete version is:
# python
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         # :type nums: List[int]
#         # :type target: int
#         # :rtype: List[int]
#         """


# They don't perform the algorithm.

# They simply describe:

# ```text
# nums   → List[int]
# target → int
# return → List[int]
# ```

# You can think of it as:

# $$
# \text{twoSum}:
# (\text{List[int]},\text{int})
# \rightarrow
# \text{List[int]}
# $$

# ---

# # 6. Class + Object Mental Model

# For coding problems, keep this simple picture in mind:

# text
#         #       CLASS
#         # ┌─────────────────┐
#         # │    Solution     │
#         # │                 │
#         # │    twoSum()     │
#         # │                 │
#         # └─────────────────┘
#         #          │
#         #          │ create object
#         #          ↓
#         # ┌─────────────────┐
#         # │     object      │
#         # │    solution     │
#         # └─────────────────┘
#         #          │
#         #          │ call method
#         #          ↓ solution.twoSum(nums, target)


# You don't need to create the object yourself on LeetCode. The platform handles that.

# ---

# # 7. Important Concepts for Your Upcoming Problems

# I'll use this **class-based format** for your future Python coding problems:

# ### Python fundamentals

# 1. Variables
# 2. Data types
# 3. Lists
# 4. Tuples
# 5. Sets
# 6. Dictionaries
# 7. Strings
# 8. `if/elif/else`
# 9. `for` loops
# 10. `while` loops
# 11. `range()`
# 12. `enumerate()`
# 13. `zip()`
# 14. Functions
# 15. `return`
# 16. List comprehensions

# ### OOP concepts

# 1. Class
# 2. Object
# 3. Method
# 4. `self`
# 5. Constructor `__init__`
# 6. Instance variables
# 7. Class variables
# 8. Inheritance — later, when needed

# ### Algorithm concepts

# We'll gradually learn:

# text
# Brute Force
#     ↓
# Time Complexity
#     ↓
# Hashing
#     ↓
# Two Pointers
#     ↓
# Sliding Window
#     ↓
# Stack / Queue
#     ↓
# Binary Search
#     ↓
# Linked List
#     ↓
# Trees
#     ↓
# Heap / Priority Queue
#     ↓
# Graphs
#     ↓
# Dynamic Programming


# For **each problem**, I'll first give you:

# **1. Concepts needed → 2. Python concepts → 3. Mathematical idea → 4. Brute-force approach → 5. Optimized approach → 6. Class-based Python code → 7. Dry run → 8. Time & space complexity.**

# That way, you're learning the **problem-solving pattern**, not just memorizing LeetCode code.


# """