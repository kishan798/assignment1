def min_elements(n, arr):
    codd = 0;
    for i in range(n):
        if(arr[i] % 2):
            codd +=1;
    return min(codd, n-codd);
if __name__ == '__main__':
    arr = [1,3,5,4,2];
    n = len(arr);
    print(min_elements(n, arr));


