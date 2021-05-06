a = [6,4,1]

swap = 0
swap1 = 1
while swap1 != 0:
    swap1 = 0
    for i in range (1,len(a),1):
        if a[i-1] > a[i]:
            temp = a[i]
            a[i] = a[i-1]
            a[i-1] = temp
            swap1 += 1
            print(swap1 ,a)
            swap += 1
print(f"Array is sorted in {swap} swaps")
print("First Element:",a[0])
print("Last Element:",a[-1])
