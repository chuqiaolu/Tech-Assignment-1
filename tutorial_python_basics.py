print("hello world")
nums = [1,2,3,4,5]
nums_double = [x*2 for x in nums] # multiply element by 2 and store in a new list
nums_squared = [x**2 for x in nums] # square each element and store in a new list
nums_subtract = [x-2 for x in nums if x>3] # subtract 2 from each element if its values is greater than 3 and store in a new list

print(nums_double) # prints [2,4,6,8,10]
print(nums_squared) # prints [1,4,9,16,25]
print(nums_subtract) #prints [2,3]; Notice only 2 elements!!!