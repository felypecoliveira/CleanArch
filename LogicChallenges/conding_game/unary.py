"""
Binary with 0 and 1 is good, but binary with only 0, or almost, is even better!

Write a program that takes an incoming message as input and displays as output the message encoded using this method.

 	Rules
Here is the encoding principle:

The input message consists of ASCII characters (7-bit)
The encoded output message consists of blocks of 0
A block is separated from another block by a space
Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
- First block: it is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0
- Second block: the number of 0 in this block is the number of bits in the series
 	Example
Let’s take a simple example with a message which consists of only one character: Capital C. C in binary is
represented as 1000011, so with this method, this gives:

0 0 (the first series consists of only a single 1)
00 0000 (the second series consists of four 0)
0 00 (the third consists of two 1)
So C is coded as: 0 0 00 0000 0 00


Second example, we want to encode the message CC (i.e. the 14 bits 10000111000011) :

0 0 (one single 1)
00 0000 (four 0)
0 000 (three 1)
00 0000 (four 0)
0 00 (two 1)
So CC is coded as: 0 0 00 0000 0 000 00 0000 0 00

"""

msg = input()
binMsg = []
for c in msg:
    # converts c to a 7digit 0 left padded binary code
    binMsg.append('{0:07b}'.format(ord(c)))

# reunites the list of string into one string and browses it, updating :
# - prev which contains the last character of binMsg read : '0' or '1'
# - count which countains the number of consecutive identical characters
# and printing the result gradually
prev, count = None, 0
for c in ''.join(binMsg):
    if c != prev:
        print(('0' * count) + \
              (' ' if count else '') + \
              ("00 " if c == '0' else "0 "), end='')
        count = 1
    else:
        count += 1
    prev = c
print("0" * count, end="")






