class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        Left = 0
        max_lenght = 0
        
        for Right in range(len(s)): 
            while s[Right] in char_set:
                char_set.remove(s[Left])
                Left += 1
            char_set.add(s[Right])
            max_lenght = max(max_lenght, Right - Left + 1)
            
        return max_lenght
    
x = input("Enter a string: ")
object = Solution()
result = object.lengthOfLongestSubstring(x)
print(result)
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         char_set = set()
#         Left = 0
#         max_lenght = 0
        
#         for Right in range(len(s)): 
#             while s[Right] in char_set:
#                 char_set.remove(s[Left])
#                 Left += 1
#             char_set.add(s[Right])
#             max_lenght = max(max_lenght, Right - Left + 1)
            
#         return max_lenght
    
# x = input("Enter a string: ")
# object = Solution()
# result = object.lengthOfLongestSubstring(x)
# print(result)




# the algorithm works like this:

# Right	Character	Set before	Action	                      Left	Window	Length	max_lenght
# 0       	a	    {}	        add a	                       0	 a	      1	       1
# 1	        b	    {a}	        add b	                       0	ab	      2	       2
# 2	        c	    {a,b}	    add c	                       0	abc	      3	       3
# 3	        a	    {a,b,c}	    remove a, add a	               1	bca       3        3
# 4	        b	    {b,c,a}	    remove b, add b	               2	cab       3	       3
# 5	        c	    {c,a,b}   	remove c, add c	               3	abc	      3	       3
# 6	        b	    {a,b,c} 	remove a, remove b, add b	   5	cb	      2	       3
# 7	        b	    {c,b}	    remove c, remove b, add b	   7	b	      1	       3