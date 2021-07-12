# print("你好，世界")

# a,b,c=1,2,3

def reverseWords(input):
    split = input.split(" ")
    inputWords = split[-1::-1]
    output = ' '.join(inputWords)
    return output


def a():
    a = set('abracadabra')
    b = set('alacazam')
    print(a)
    print(b)
    print(a - b)
    print(a | b)
    print(a & b)
    print(a ^ b)


'''
多行注释
'''
if __name__ == '__main__':
    '''
    input = 'I Like runoob'
    rw = reverseWords(input)
    print(rw)
    a()
    '''
    a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
    a.append([1,2,3])
    a.extend([1,2,3])
    print(a)
    '''for i in range(len(a)):
        print(i,a[i])'''


