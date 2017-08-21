import random, time, sys
class colors():
    red =  "\u001b[31m"
    green =  "\u001b[32m"
    yellow =  "\u001b[33m"
    blue =  "\u001b[34m"
    magenta = "\u001b[35m"
    cyan =  "\u001b[36m"
n =  "\u001b[0m"
renkler = [colors.red, colors.green, colors.yellow, colors.blue, colors.magenta, colors.cyan]
def loading():
    global bitis
    finish = False
    c = 1
    while not finish:
        place = c%20
        string ="["+" "*17+"]"
        liste = list(string)
        first = "❯"
        second = "❯"
        third = "❯"
        if place == 1:
            liste[place] = random.choice(renkler)+first+ n
        if place == 2:
            liste[place] =random.choice(renkler) + first+ n
            liste[place - 1] = random.choice(renkler)+second + n
        if place > 2:
            if place <18:
                liste[place] =random.choice(renkler) +first + n
                liste[place -1] =random.choice(renkler)+second+ n
                liste[place-2] =random.choice(renkler)+third +n
        if place == 18:
            liste[place -2] =random.choice(renkler)+ third+n
            liste[place - 1] =random.choice(renkler)+second +n
        if place == 19:
            liste[place-2] =random.choice(renkler)+ third+n
                
        
        liste = "".join(liste)
        sys.stdout.write("\r "+liste)
        c += 1
        time.sleep(.1)
if __name__=="__main__":
    loading()