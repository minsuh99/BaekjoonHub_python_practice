K = int(input())
head_list=[]
for k in range(K):
    h = int(input())
    action = [i for i in input()]
    
    for act in action:
        if act == 'c':
            h += 1 
        elif act == 'b':
            h -= 1
        if h == 0:
            break
    head_list.append(h)

for k in range(K):
    print(f"Data Set {k+1}:")
    print(head_list[k])
    if k != K-1:
        print()