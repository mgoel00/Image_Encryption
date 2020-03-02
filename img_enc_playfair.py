import string
import itertools


def chunker(seq,size):
    n = int(size/2)
    for i in range(n):

        chunk = ( seq[i],seq[(n+i)%n] )
        if not chunk:
            return
        yield chunk



def cleaner(plaintext,value):

    clean = []

    for i in range(len(plaintext)-1):
        clean.append(plaintext[i][value])

        

    clean.append(plaintext[-1])
    # if len(clean) & 1:
    #     clean.append(175) 

    return clean


def generate_table(key):
    alphanumeric = [i for i in range(256)]
    table = []

    for i in key:
        if i not in table and i in alphanumeric:
            table.append(i)

    for i in alphanumeric:
        if i not in table:
            table.append(i)

    return table


def cipher(plaintext,key,size,value):
    table = generate_table(key)
    plaintext = cleaner(plaintext,value)

    ciphertext = []


    for char1,char2 in chunker(plaintext , size):
        row1, col1 = divmod(table.index(char1),16)
        row2, col2 = divmod(table.index(char2),16)

        if row1 == row2:
            ciphertext.append(table[row1*16 + (col1+1)%16])
            ciphertext.append(table[row2*16 + (col2+1)%16])
        elif col1 == col2:
            ciphertext.append(table[((row1+1)%6)*16 + col1])
            ciphertext.append(table[((row2+1)%6)*16 + col2])
        else:
            ciphertext.append(table[row1*16 + col2])
            ciphertext.append(table[row2*16 + col1])

    return ciphertext
