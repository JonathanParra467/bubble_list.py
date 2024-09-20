# Create a python script that asks user for 5 integer values (in any order).
# Store those numbers in a list
# Sort the list in ascending order
# Display the list
nums = []
for i in range(5):
    num = int(input("enter a number: "))
    nums.append(num)

swapped = True
while swapped:
    swapped = False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            swapped = True
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
print(nums)
