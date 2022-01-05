print("Assalomu alaykum bu dastur matematika olamida hali yechilmagan eng oson jumboqlardan biri bo'lgan ",end="")
print("3x+1 ga bag'ishlanadi,ya'ni x ning istalgan natural qiymatida bu oxir oqibat 4,2,1 sirtmog'iga tushadi")
input("keling buni men amalda ko'rsataman. Davom etish uchun biror tugmani bosing.")
ishora=True
while ishora:
    son=int(input("Biror son kiriting: "))
    kollatsa=[]
    while son!=1:
        if son%2==0:
            son/=2
            kollatsa.append(int(son))
        elif son%2!=0:
            son=(son*3)+1
            kollatsa.append(int(son))
    jadval=str(kollatsa)
    print(jadval)
    savol=input("Agarda ishonmagan bo'lsangiz yana sinab ko'ring(ha=1,yo'q=0) ")
    if savol!="1":
        ishora=False
        print("Bu shunchaki generator,isbot emas.")
    else:
        print("Lekin bu befoyda  chunki har doim kiritgan soningiz sirtmoqdan qochib qutula olmaydi.",end="")
        input("MAyli yana bir marta o'ynash uchun ENTER ni bosing")                

        