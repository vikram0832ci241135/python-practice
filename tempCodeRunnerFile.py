a = [12,14,16,23,25,34,37,45,48,59,68,70]

search = 45

start = 0
last = len(a)-1
mid = (start + last)//2

while start <= last:
    if a[mid] == search:
        print (f"element found at index {mid}")
        break

    elif a[mid] < search:
        start = mid + 1
        mid = (start + last)//2

    elif a[mid] > search:
        last = mid - 1
        mid = (start +  last)//2
else:
    print("sorry your no is not exist")