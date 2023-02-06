import time

initial = time.time()

k = 0
while (k < 45):
    print("This is hjr")
    time.sleep(2)
    k += 1
print("While loop ran in", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(45):
    print("This is jnfj")
print("For loop ran in", time.time() - initial2, "Seconds")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

