'''
atoi - convert a string to an integer
itoa - convert an integer to a string
'''

class atoi_itoa:

    def atoi(self,inp):
        if len(inp) == 0:
            return 0
        sign = 1
        i = 0
        if inp[0] == '-':
            sign = -1
            i+=1
        res = 0
        for x in range(i,len(inp)):
            if (inp[x] < '0' or inp[x] > '9'):
                return 0
            res=res*10 + (ord(inp[x]) - ord('0'))
        return sign*res

    def itoa(self,inp):
        res = ""
        sign = ""
        if(inp < 0):
            inp *= -1
            sign = "-"
        while(inp > 0):
            res += str(inp%10)
            inp = inp / 10
        res += sign
        return res[::-1]


if __name__ == '__main__':
    obj = atoi_itoa();
    input_data = raw_input("Enter to convert from atoi: ")
    plain_text = obj.atoi(input_data)
    print(plain_text)
    input_data = raw_input("Enter to convert from itoa: ")
    plain_text = obj.itoa(int(input_data))
    print(plain_text)
