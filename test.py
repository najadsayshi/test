a=[1,2,3,4,5,6,7]

largest=a[0]
secondlargest=-1

for i in range(1,len(a),1):
    if a[i]>largest:
        secondlargest=largest
        largest=a[i]
    elif a[i]<largest and a[i]>secondlargest:
        secondlargest=a[i]
print(secondlargest)