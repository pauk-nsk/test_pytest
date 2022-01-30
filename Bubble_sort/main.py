def sort_bubble(spisok):
    N=len(spisok)
    for i in range(N-1):
        for j in range(N-i-1):
            if spisok[j] > spisok[j+1]:
                buff = spisok[j]
                spisok[j] = spisok[j+1]
                spisok[j+1] = buff
    return spisok

#тестовые наборы
#list=[4,3,7,9,3,6,8,3,1,6]
list=[4,6,9,2,8,230,560,234,345,268,934,239]
#list=[4.9899,6,9,2.768,8.67,230,560,234.78,345.768678,268,934,239]
#list=[4.9899,6,'text',2.768,8.67,230,560,234.78,345.768678,268,934,239]
#list=[5,6,9,2,5,6,560,5,6,268,5,239]
print(list)
sort_bubble(list)
print(list)
