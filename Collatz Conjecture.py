import time
import matplotlib.pyplot as plt

n = 0
end = 1
count = 0
highestNumber = 0
xAxis = []
yAxis = []


print("Input Starting Number!")
n = int(input())

while True:

    if n == end:
        print(n)
        print("Collatz Conjecture went to 1 in", count,
              "steps! The highest number it reached was", highestNumber)
        break

    elif n != end:
        print(n)

        if n > highestNumber:
            highestNumber = n

        count = count+1
        xAxis.append(count)
        yAxis.append(n)
        # time.sleep(0.025)

        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n+1

plt.plot(xAxis, yAxis)
plt.xlabel('# of Steps')
plt.ylabel('Hailstone #s')
plt.title("Collatz Conjecture")

# print("xaxis:", xaxis)
# print("yaxis:", yaxis)

plt.show()
