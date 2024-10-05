# Count the number of elements in heights that are not in their expected sorted order
# heights= [1,1,4,2,1,3]
# expected = [1,1,1,2,3,4]
# output: 3

heights= [1,1,4,2,1,3,6]
expected = [1,1,1,2,3,4,7]
count=0
for i in range(len(heights)):
    if heights[i]!=expected[i]:
        count+=1
print(count)
