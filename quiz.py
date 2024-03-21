import time
print(25*' ',"welcome to Anime Quiz")
print(25*' ',"*********************")
print(25*' ',"*********************")

dic={"1.Choose one anime who's story is NINJA ":'A',
     "2.Naruto likes_____in his childhood":"D",
     "3.Hinata has ?":"C",
     "4.Sasuke last name is?":"B",
     "5.Naruto married?":"C",
     "6.Roclee has_____ power":"D",
     "7.Name the team7 members":"B",
     "8.who use shadow clone jutsu":"A",
     "9.what is the name of the naruto village":"D",
     "10.Who is 7th Hokage":"A"}
opt=[['A.NARUTO','B.THE DEATH NOTE','C.ONE PUNCH MAN','D.THE ONE PIEACE'],["A.HINATA",'B.KAKASHI','C.SASUKE','D.SAKURA'],['A.FEAR','B.BEAUTY','C.HYAKUGUN','D.SHY'],["A.HATAKE",'B.UCHIHA','C.UZUMAKI','D.HYUGA'],['A.SAKURA','B.INO','C.HINATA','D.TINTIN'],['A.RASENGAN','B.CHIDORI','C.HYAKUGUN','D.LOTUSFLOWER'],['A.Rock Neji TinTin','B.Naruto Sasuke Sakura','C.Shikamaru Ino Choji','D.Hinata Akamaru Kasdn'],['A.Shikamaaru','B.Hinata','C.Ino','D.Sakura'],['A.SAND VILLAGE','B.MIST VILLAGE','C.WATER VILLAGE','D.LEAF VILLAGE'],['A.NARUTO UZUMAKI','B.TSUNADE','C.KAKASHI HATAKE','D.SASUKE UCHIHA']]
#print(opt[0])
QNO=1
score=0
for i in dic:
    print("------------------------------------------------------------")
    time.sleep(1)
    print(i)
    time.sleep(1)
    for j in opt[QNO-1]:
        print(j)
    print(" ")    
    choice=input("enter ur choice: ").upper()
    if(choice==dic[i]):
        #print("WOW!!! U R Amazing ")
        score+=1
    #else:
        #print("U IDIOT ,DO'T U KNOW MATHS") 
    QNO+=1 
print("*****************************************************************************")      
print(25*' ',"Thank u for participating.......")     
time.sleep(3)        
print(25*' ',"UR Total Score = ",score)