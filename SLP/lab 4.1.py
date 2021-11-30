def calculateMean(list):
    sum = 0
    for i in list:
        sum += i
    mean = sum / len(list)

    return round(mean, 2)


print(f"Mean of the list:", calculateMean([1, 2, 3, 4, 5, 6]))