# รับ array จำนวนเต็ม แบ่ง array 2 array ที่มีผลรวมเท่ากัน Return Yes No
test1 = [1,2,3,4,2]
test2 = [1,1,1,1,9,2,2,2,2,7]
test3 = [1,2,3,4,5,6]

def array_two_sum(nums):
    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    current_sum = 0
    subset = []
    selected_indices = []

    for i in range(len(nums)):
        current_sum += nums[i]
        subset.append(nums[i])
        selected_indices.append(i)

        if current_sum == target_sum:
            # Create the two sublists
            list1 = [nums[j] for j in selected_indices]
            list2 = [nums[j] for j in range(len(nums)) if j not in selected_indices]
            return list1, list2

        # If the current sum exceeds the target sum, backtrack and try a different combination
        while current_sum > target_sum:
            current_sum -= subset[0]
            subset.pop(0)
            selected_indices.pop(0)

            # If there are no more elements to remove, break the loop
            if len(subset) == 0:
                break

            # Check if the current sum equals the target sum after backtracking
            if current_sum == target_sum:
                # Create the two sublists
                list1 = [nums[j] for j in selected_indices]
                list2 = [nums[j] for j in range(len(nums)) if j not in selected_indices]
                return list1, list2


    return False



print(array_two_sum(test1)) #expected True
print(array_two_sum(test2)) #expected True
print(array_two_sum(test3)) #expected False
