def get_unique_list(num_list1):
    unique=[]
    for i in num_list1:
        if i not in unique:
            unique.append(i)
    print(unique)
num_list1=[1,2,5,2,5,1,3,7,9]
get_unique_list(num_list1)