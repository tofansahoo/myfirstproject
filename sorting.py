#class A:
#     def show(self):
#         print("in A show")
# class B(A):
#     def show(self):
#          print("in B show")
# a1 = A()
# a1.show()
# Example 2
# pos = -1
# def search(list, n):
#       i = 0
#       while i< len(list):
#             if list[i] == n:
#                 globals()['pos'] = i
#                 return True
#             i = i+1
#       return False
# 
# list = [5,8,6,4,9,2]
# n = 9
# 
# if search(list, n):
#     print("Found at ", pos+1)
# else:
#     print("Not Found")
