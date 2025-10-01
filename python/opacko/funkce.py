def sumOfNums(num1, num2):
    return num1 + num2


def sumOfNums2(*nums):
    return sum(nums)

def showNums(*nums):
    for i in nums:
        print(i, end=" * ")

s = sumOfNums

print(s(25, 25))
print(sumOfNums(25, 25))
print(sumOfNums(sumOfNums(5, -14), sumOfNums(9, -6)))

print(sumOfNums2(25, 64, -42, 67))

print(showNums(5, 8, 3, 8))