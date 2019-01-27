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
# Example Linear Search
# pos = -1
# def forsearch(list,n):
# #    i = 1
#     for i in range(1, len(list)):
#         if list[i] == n:
#             globals()['pos']=i
#             return True
#     return False
#
# list = [5,8,6,4,9,2]
# n = 9
#
# if forsearch(list,n):
#     print("Found at ",pos+1)
# else:
#     print("Not Found")
# Example Biary search
# pos = -1
# def search(list, n):
#     L = 0
#     U = len(list)-1
#     while L <= U:
#         mid = (L+U) // 2
#         if list[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list[mid] < n:
#                 L = mid + 1
#             else:
#                 U = mid - 1
#     return False
#
# lst = [5,8,6,4,9,2,99,230,85,72,120,2200]
# list = sorted(lst)
#
# n = 100
# if search(list,n):
#     print("Found at ",pos+1)
# else:
#     print("Not Found")
