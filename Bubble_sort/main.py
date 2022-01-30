def sort_bubble(spisok):
    N=len(spisok)
    for i in range(N-1):
        for j in range(N-i-1):
            if spisok[j] > spisok[j+1]:
                buff = spisok[j]
                spisok[j] = spisok[j+1]
                spisok[j+1] = buff
    return spisok

'''list=[4,6,9,2,8,230,560,234,345,268,934,239]
print(list)
sort_bubble(list)
print(list)'''
