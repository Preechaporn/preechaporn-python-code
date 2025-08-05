def add(a,b):
    total = a+b
    print("inside add : ",total)
    return total

if __name__ == "__main__" :

    my_sum = 0
    for i in range(3) :
        total = add(1,2)
        
        my_sum += total
        print("inside main : ",my_sum)