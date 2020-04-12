input1 = 3
input2 = ['1jamesro', '1jamesro', '3jamesro', '5jamesro', '1jamesro']

alist = []

lists = []

for my_string in input2:
    count = 0
    for letter in my_string:
        my_string = my_string[-1] + my_string[:-1]
        alist.append(my_string)
    lists.append(alist)
    count +=1
count = 0

print(lists)
for i in range(len(lists)):
    try:
        alist = lists[0][i]

        blist = sorted(lists[0][i+1])
       
        if alist[0] == blist[0]:

            count+=1
            continue
        
        for passwordA in alist:
            if passwordA in blist:
                count+=1
                break
        

    except:
        print('end of list')
        

print(count)