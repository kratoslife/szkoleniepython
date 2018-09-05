#f = open('C:/lala.txt')
#l=f.readline()
#print(l)

with open('C:/lala.txt') as f:
    sum=0
    for l in f.readlines():
        print(l)
        sum=sum+int(l)
    print(sum)
#    print('"%s"' % f.readline().strip())
#    print(f.readline())
#    print(f.readline())
#    print(f.tell())






#with open('C:/lala.txt') as f:
#    for l in f.readlines():
#        print(l.strip())


#with open('C:/lala.txt') as f:
#    for l in f:
#        print(l[:-1])