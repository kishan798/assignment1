def Max_occurence(str):
    ASCII_SIZE = 256
    count= [0] * ASCII_SIZE
    max = -1
    c = ''
    for i in str:
        count[ord(i)]+=1;
    for i in str:
        if (max < count[ord(i)]):
            max = count[ord(i)]
            c = i;
    return c;
str = "aaaaaaaabbbcddddeeee"
print(Max_occurence(str))

