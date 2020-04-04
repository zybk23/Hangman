import random


class HangMan(object):
    # Hangman game
    hang = []
    hang.append(' +---+')
    hang.append(' |   |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('=======')

    man = {}
    man[0] = [' 0   |']
    man[1] = [' 0   |', ' |   |']
    man[2] = [' 0   |', '/|   |']
    man[3] = [' 0   |', '/|\\  |']
    man[4] = [' 0   |', '/|\\  |', '/    |']
    man[5] = [' 0   |', '/|\\  |', '/ \\  |']

    pics = []

    words = '''Duru Yakamoz Toprak
Çiselemek
Birlik
Üstad
Hazan
Işıl
Dandik
Başak
Vatan
Gönenç
Hayat
Gökyüzü
Deniz
Gönül
Kof
Kutlu
Barış
Sevmek, sövmek
Sarmak, sürmek
Dudu
Cennet cinnet
Kelam
Devrim Aşk
Bilakis
Deniz
Yasal
Cemre
Vuslat
Yeniden
Doğu
Mut
Asya
Asel
Beyoğlu
Efsun
Efkar
Su
Yürek
Dost
Şıpır şıpır
Şatafatlı
Şen şakrak
Peki
Hayal
Ender
Yasemin
Çiğdem
Figen
Sude
Hasret
Kem küm
Damarına basmak'''.split()

    infStr = '_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\''

    def __init__(self,*args,**kwargs):

        i,j=2,0
        self.pics.append(self.hang[:])
        for ls in self.man.values():
            pic,j=self.hang[:],0
            for m in ls:

                pic[i+j]=m
                j+=1
            self.pics.append(pic)

    def pickWord(self):
        return self.words[random.randint(0,len(self.words)-1)]

    def printPic(self,idx,iwordLen):
        for line in self.pics[idx]:
            print(line)

    def askAndEvaluate(self,word,result,missed):
        guess=input()

        if guess==None or len(guess)!=1 or (guess in result) or guess in missed :

            return None,False
        i=0

        right =guess in word

        for c in word :
            if c==guess:
                result[i]=c
            i+=1

        return guess , right

    def info(self,info):
        ln=len(self.infStr)
        print(self.infStr[:-3])
        print(info)
        print(self.infStr[3:])
    def start(self):
        print("Hangman'e Hoş Geldin !")

        word=list(self.pickWord())
        result=list("*"*len(word))
        print("Kelime : ",result)
        success , i , missed =False , 0 , []

        while i < len(self.pics)-1:
            print("Kelimeyi Tahmin Et Bakalım :",end=" ")
            guess , right = self.askAndEvaluate(word,result,missed)
            if guess==None :
                print("Bu harfi daha önceden girmiştin")
                continue
            print("".join(result))
            if result == word:
                self.info("Tebrikler! Bir Hayat Kurtardın !")
                success = True
                break
            if not right:
                missed.append(guess)
                i+=1
            self.printPic(i,len(word))
            print("Kullanılan Harfler :",missed)
        if success==False :
            self.info('Kelime \''+''.join(word)+'\'+"dı"+ ! Sadece Basit Bir Kelimeydi , Bilemedin  !')


a=HangMan().start()