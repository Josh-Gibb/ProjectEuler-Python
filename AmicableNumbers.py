import math

# A method that returns the sum of all factors
def sumOfFactors(number):
    sum = 1
    for i in range(2, int(math.sqrt(number))+1):
        if(number%i == 0):
            sum += i
            if(i != number // i):
                sum += number // i;
    return sum

# A method that finds the sum of all amicable numbers below num
def amicableNumbers(num):
    amicableNum = set();
    for i in range(1, num):
        if i not in amicableNum:
            a = sumOfFactors(i)
            if(a != i and sumOfFactors(a) == i):
                amicableNum.add(a)
                amicableNum.add(i)
    return sum(amicableNum)

def main():
    print(amicableNumbers(10000))

if __name__ == "__main__":
    main()
