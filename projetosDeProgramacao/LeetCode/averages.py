




def minimumAverage(nums: list[int]) -> float:
    averages = []

    #sort nums
    i = 0
    nums.sort()

    while nums != []:

        minElement = nums.pop(0)
        maxElement = nums.pop()

        avg = (minElement + maxElement) / 2

        averages.append(avg)

        print(f"minElement = {minElement}, maxElement = {maxElement}, averages = {averages}")

        i += 1

    averages.sort()


    return (averages[0])


L = [7,8,3,4,15,13,4,1]



minimumAverage(nums = L)