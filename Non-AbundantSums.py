# A method to find the sum of factors
def sumOfFactors(num):
    total = 1
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i == 0):
            total += i
            if (num // i != i):
                total += num // i
    return total

# A method to store all abundant numbers less than limit
def getAbundantNumbers(limit):
    abundantNumbers = set()
    for i in range(12, limit):
        if i < sumOfFactors(i):
            abundantNumbers.add(i)
    return abundantNumbers

# A method to get the sum of all non abundant numbers less than limit
def sumOfNonAbundantNumbers(limit):
    numbers = set()
    total = sum(range(1, limit + 1))
    abundantNum = getAbundantNumbers(limit)
    for a in abundantNum:
        for b in abundantNum:
            if (a + b > limit):
                break
            numbers.add(a + b)
    return total - sum(numbers)


def main():
    print(sumOfNonAbundantNumbers(28123))


if __name__ == "__main__":
    main()
