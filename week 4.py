list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
def even_test(lst):
    for x in lst:
        if x%2 ==0:
            print (x)

even_test(list1)

list2= [2, 3, 10, 14, 20, 21, 25, 13, 15]
list3=[k for k in list2 if k**2 >150]
print (list3)

list4 = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
list5 = [k for k in set(list4) if k%2==0]
print(type(list5))


def process_string(s):
    k = s.split()
    print (k)

    for x in range(len(k)):
        print (x)
        if x%2 ==0:
            print(k[x].lower())
        else: print(k[x].upper())

print(process_string("This is my test String"))




def get_five():
    return 5
def get_and_print_five():
    five = get_five()
    print(f'Called get_five(): result is {five}')


get_and_print_five()


number = 2323