# processing list elements in single line
# comprehension

nums=[1,2,3,4]

print("old array" , nums)
#Adding 10 to each element in the list
nums = [(item + 10) for item in nums ]
print("new array" , nums)