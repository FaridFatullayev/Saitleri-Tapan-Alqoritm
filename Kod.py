cumle = input('cumleni yazin: ')
sait = "a,ı,o,u,e,ə,i,ö,ü"
S=0
for i in cumle:
    if i in sait:
        print("Saitler bunlardir ", i)
        S=S+1
print("Sayi : " ,S)
