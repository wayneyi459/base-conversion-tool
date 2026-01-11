#任意进制转换
def main():
    num = input('Enter the number: ')
    base = int(input('Enter the base of the number: '))
    target = int(input('Enter the base you want to be: '))
    print(numSwitft(toDecimal(num, base), target))

def toDecimal(num:str, base): 
    sequence = '0123456789ABCDEF'
    count = 0
    for i in num:
        size = sequence.index(i)
        count = count * base + size
    return count

def numSwitft(num:int, base):
    sequence = '0123456789ABCDEF'
    if num < base:
        return sequence[num]
    else:
        return numSwitft(num // base, base) + sequence[num % base]

main()