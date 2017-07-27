'''
The code you will write is based on the “Caesar Cipher” where each letter is shifted a certain number of places left or right through the alphabet.
The alphabet is treated as being circular so that the first letter follows after the last letter, and the last letter precedes the first letter.
These ideas will be applied separately to uppercase letters, lower case letters, and digits.
For example, with a shift of 1, ‘A’ becomes ‘B’, ‘Z’ becomes ‘A’, ‘a’ becomes ‘b’, ‘z’ becomes ‘a’, ‘0’ becomes ‘1’, ‘9’ becomes ‘0’.
Spaces, punctuation, and any other symbols are unaffected in this scheme.
Your task is to write a function to encrypt a string using this Caesar Cipher. 

INPUT FORMAT
Your function will take an input string that begins with a number representing the shift.
The number will be in the range -1000000000 to 1000000000 (negative 1 billion to 1 billion).
The number is followed by a colon (‘:’).
The rest of the line consists of a string of 1 to 200 arbitrary characters and represents a fragment of the text to be encrypted.
 
OUTPUT FORMAT
Output will be the corresponding encrypted text fragment
  
SAMPLE INPUT:
1:some text
 
SAMPLE OUTPUT:
tpnf ufyu
'''

class Ceasar:

    def parseInput(self, input_data):
        num, plain_text = input_data.split(":")
        n = int(num)
        self.n = n
        return plain_text

    def shiftDigit(self, c):
        n = self.n
        if self.n < 0:
            n = (10 - (abs(self.n) % 10)) % 10
        v = chr((ord(c) - ord('0') + n) % 10 + ord('0'))
        return v

    def shiftAlpha(self, c):
        n = self.n
        if self.n < 0:
            n = (26 - (abs(self.n) % 26)) % 26
        v = chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        return v

    def encrypt(self, text):
        r = ''
        for c in list(text):
            if c.isdigit():
                r += self.shiftDigit(c)
            elif c.isalpha():
                if(c.isupper()):
                    r += (str(self.shiftAlpha(c.lower()))).upper()
                else:
                    r += str(self.shiftAlpha(c))
            else:
                r += c
        return r

if __name__ == '__main__':
    e = Ceasar();
    input_data = raw_input("Enter: ")
    plain_text = e.parseInput(input_data)
    print(e.encrypt(plain_text))
