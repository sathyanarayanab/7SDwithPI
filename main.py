import RPi.GPIO as GPIO
import time
import string
import os, sys

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

#setup output pins

pins = [2,3,4,17,27,22,10,9]
for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
 
#define 7 segment digits

digitclr=[1,1,1,1,1,1,1,1]
digit0=[0,0,0,0,0,0,1,1]
digit1=[1,0,0,1,1,1,1,1]
digit2=[0,0,1,0,0,1,0,1]
digit3=[0,0,0,0,1,1,0,1]
digit4=[1,0,0,1,1,0,0,1]
digit5=[0,1,0,0,1,0,0,1]
digit6=[0,1,0,0,0,0,0,1]
digit7=[0,0,0,1,1,1,1,1]
digit8=[0,0,0,0,0,0,0,1]
digit9=[0,0,0,1,1,0,0,1]

#define 7 segment letters

a=[0,0,0,1,0,0,0,1]
b=[1,1,0,0,0,0,0,1]
c=[0,1,1,0,0,0,1,1]
d=[1,0,0,0,0,1,0,1]
e=[0,1,1,0,0,0,0,1]
f=[0,1,1,1,0,0,0,1]
g=[0,0,0,0,1,0,0,1]
h=[1,1,0,1,0,0,0,1]
i=[1,1,1,0,1,1,1,0]
j=[1,0,0,0,1,1,1,1]
k=[1,0,0,1,0,0,0,0]
l=[1,1,1,0,0,0,1,1]
m=[0,0,0,1,0,0,0,0]
n=[1,1,0,1,0,1,0,1]
o=[0,0,0,0,0,0,1,1]
p=[0,0,1,1,0,0,0,1]
q=[0,0,0,1,1,0,0,1]
r=[1,1,1,1,0,1,0,1]
s=[0,1,0,0,1,0,0,1]
t=[1,1,1,0,0,0,0,1]
u=[1,0,0,0,0,0,1,1]
v=[1,1,0,0,0,1,1,1]
x=[0,1,0,0,1,0,1,1]
y=[1,1,1,1,0,0,0,1]
z=[1,0,1,1,0,1,0,1]
null=[1,1,1,1,1,1,1,0]

gpin=[2,3,4,17,27,22,10,9]

#routine to clear and then write to display

def digdisp(digit):
    # for x in range (0,8):
        # GPIO.output(gpin[x], digitclr[x])
    for x in range (0,8):
        GPIO.output(gpin[x], digit[x])
        
def letdisp(letter):
    for x in range (0,8):
        GPIO.output(gpin[x], letter[x])

def cleanup():
    GPIO.cleanup()
    sys.exit()

def calctime(start_time):
    print(f"\nTotal time taken to display : {round(time.time()-start_time,2)}")
    print("\nPlease add 1 second from the above result if you need execution time after input, as script will wait for 1 second after input from the user which is not included above\n")

digdisp(digitclr)
word = input("Enter anything to display will try my best\n\n")
word = list(word.lower())
actions = {"a":a,"b":b,"c":c,"d":d,"e":e,"f":f,"g":g,"h":h,"i":i,"j":j,"k":k,"l":l,"m":m,"n":n,"o":o,"p":p,"q":q,"r":r,"s":s,"t":t,"u":u,"v":v,"x":x,"y":y,"z":z}
digiaction={"0":digit0,"1":digit1,"2":digit2,"3":digit3,"4":digit4,"5":digit5,"6":digit6,"7":digit7,"8":digit8,"9":digit9}
time.sleep(1)

try:
    current_time = time.time()
    for i in word:
        digdisp(digitclr)
        time.sleep(0.5)
        if i.isalpha(): 
            action = actions.get(i,null)
            letdisp(action)
        elif i.isnumeric():
            action = digiaction.get(i,null)
            digdisp(action)
        else:
            digdisp(null)
        time.sleep(0.5)

except:
    print("\nForcing to exit! Cleaning up GPIO\n")
    cleanup()

calctime(current_time)
cleanup()


#GPIO Setup
# GPIO2 - a
# GPIO3 - b
# GPIO4 - c
# GPIO17 - d
# GPIO27 - e
# GPIO22 - f
# GPIO10 - g
# GPIO9 - h
# PIN1  - C
# PIN7 - C