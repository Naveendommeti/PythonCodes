#Find the common elements in a lists using Set (&) intersection
# def common_elements(num1, num2):
#     return list(set(num1)&set(num2))
# num1 = [1,2,3,4,5]
# num2 = [5,6,7,8,9,11]
# elements = common_elements(num1, num2)
# print("Common Elements", elements)

#Unique elements in a list using set()
def unique_list(n):
    return list(set(n))
list_num = [1,2,3,4,4,5,5,1,5,6]
unique_num = unique_list(list_num)
print("Unique elements: ", unique_num)