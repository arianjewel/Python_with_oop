def find_fib(n):
    if n<=2:
        return 1
    fib_x,fib_next=1,1
    i=3
    while i<=n:
        i+=1
        fib_x,fib_next=fib_next,fib_x+fib_next
    return fib_next

def list_fib(n):
    li=[1,1]
    if n<=2:
        return li[:n]
    fib_x,fib_next=1,1
    i=3
    while i<=n:
        i+=1
        fib_x,fib_next=fib_next,fib_x+fib_next
        li.append(fib_next)
    return li
if __name__=='__main__':
    for i in range(1,11):
        print(find_fib(i))

    input=int(input('how much fibonacci number do you wanna see in list: '))
    print(list_fib(input))
