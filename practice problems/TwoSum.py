# the problem is find the index of the elements in the sheet that add up to the target
# so here my input is nums and target and the nums[3] and nums [1] in summ gives  me my target 6
nums = [1, 2, 3, 4]
target = 6

# taking every element from nums and adding every other element except for the first.
# in order ot avoid repitition
for i in range(len(nums)):
  for k in range(len(nums[1:])):

    answer = nums[i]
    answer += nums[k]

    if answer == target and nums[k] != nums[i]:

      print([nums[i]-1, nums[k]-1])
      break

#final output is 3 1


