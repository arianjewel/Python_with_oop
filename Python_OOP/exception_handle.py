#program crush for exception
'''def div(a,b):
    return a/b

print(div(10,2))
print(div(3,0))
print(div(9,3))'''



#handle exception
'''def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('can\'t divide by zero')
    except TypeError:
        print('unsupported type. did you use string?')

print(div(10,2))
print(div(3,0))
print(div(9,3))
print(div('12',3))'''




import io
file_name=input('please enter your file name: ')
mode=input('please enter mode: ')

try:
    with  open(file_name,mode) as f:
        content=f.read()
        print(content)

except Exception as e:
    print(e)

'''except FileNotFoundError:
    print(file_name,'not found. please check if the file\'s name is correct')
except io.UnsupportedOperation:
    print('are you sure',file_name,'is readable?')'''
