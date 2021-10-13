import requests
import RPi.GPIO as GPIO
import time
import requests


url = 'http://192.168.0.100:8080/Insert'
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN)#pivote
GPIO.setup(23,GPIO.IN)#SWITCH
GPIO.setup(16, GPIO.OUT)#E
GPIO.setup(20, GPIO.OUT)#D
GPIO.setup(21, GPIO.OUT)#C
GPIO.setup(6, GPIO.OUT)#F
GPIO.setup(19, GPIO.OUT)#G
GPIO.setup(13, GPIO.OUT)#B
GPIO.setup(26, GPIO.OUT)#A
GPIO.setup(12, GPIO.OUT)#reley

dato = 0

def uno():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(26, False)#A
    GPIO.output(13, True)#B
    GPIO.output(21, True)#C
    GPIO.output(20, False)#D
    GPIO.output(16, False)#E
    GPIO.output(6, False)#F
    GPIO.output(19, False)#G
    GPIO.output(12, False)#reley
    
def dos():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(26, True)#A
    GPIO.output(13, True)#B
    GPIO.output(21, False)#C
    GPIO.output(20, True)#D
    GPIO.output(16, True)#E
    GPIO.output(6, False)#F
    GPIO.output(19, True)#G
    GPIO.output(12, False)#reley

def tres():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(26, True)#A
    GPIO.output(13, True)#B
    GPIO.output(21, True)#C
    GPIO.output(20, True)#D
    GPIO.output(16, False)#E
    GPIO.output(6, False)#F
    GPIO.output(19, True)#G
    GPIO.output(12, True)#reley

def cuatro():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(26, False)#A
    GPIO.output(13, True)#B
    GPIO.output(21, True)#C
    GPIO.output(20, False)#D
    GPIO.output(16, False)#E
    GPIO.output(6, True)#F
    GPIO.output(19, True)#G
    GPIO.output(12, True)#reley

def cinco():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(26, True)#A
    GPIO.output(13, False)#B
    GPIO.output(21, True)#C
    GPIO.output(20, True)#D
    GPIO.output(16, False)#E
    GPIO.output(6, True)#F
    GPIO.output(19, True)#G
    GPIO.output(12, True)#reley
    
def seis():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(26, True)#A
    GPIO.output(13, False)#B
    GPIO.output(21, True)#C
    GPIO.output(20, True)#D
    GPIO.output(16, True)#E
    GPIO.output(6, True)#F
    GPIO.output(19, True)#G
    GPIO.output(12, True)#reley

def siete():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(26, True)#A
    GPIO.output(13, True)#B
    GPIO.output(21, True)#C
    GPIO.output(20, False)#D
    GPIO.output(16, False)#E
    GPIO.output(6, False)#F
    GPIO.output(19, False)#G
    GPIO.output(12, False)#reley

def ocho():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(26, True)#A
    GPIO.output(13, True)#B
    GPIO.output(21, True)#C
    GPIO.output(20, True)#D
    GPIO.output(16, True)#E
    GPIO.output(6, True)#F
    GPIO.output(19, True)#G
    GPIO.output(12, True)#reley
    
def nueve():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(26, True)#A
    GPIO.output(13, True)#B
    GPIO.output(21, True)#C
    GPIO.output(20, False)#D
    GPIO.output(16, False)#E
    GPIO.output(6, True)#F
    GPIO.output(19, True)#G
    GPIO.output(12, False)#reley

def cero():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(26, True)#A
    GPIO.output(13, True)#B
    GPIO.output(21, True)#C
    GPIO.output(20, True)#D
    GPIO.output(16, True)#E
    GPIO.output(6, True)#F
    GPIO.output(19, False)#G
    GPIO.output(12, True)#reley
    
def nada():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(26, False)#A
    GPIO.output(13, False)#B
    GPIO.output(21, False)#C
    GPIO.output(20, False)#D
    GPIO.output(16, False)#E
    GPIO.output(6, False)#F
    GPIO.output(19, False)#G
    
def base(tiempo,contador):
    url = 'http://192.168.0.100:8080/Insert'
    body = {"object_to_insert": {"Dispositivo":"RaspberrypiBALR","Fecha" : tiempo, "Valor Contador" : contador }} #Crear uno por cada objeto que se desee insertar en la base, el campo "object_to_insert" es obligatorio
    resp = requests.post(url, json=body)
    print(resp.status_code)
    print(resp.json())

while True:
    if GPIO.input(22):
        if GPIO.input(23):
            tiempo = f"{time.localtime().tm_mday}/{time.localtime().tm_mon}/{time.localtime().tm_year} , {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}"
            dato = dato + 1
            url = 'http://1f73-190-104-112-77.ngrok.io/data/%s' % dato 
            urlget = requests.get(url)
            x = str(urlget.text)
            print(x)
            if x == '11110110':#9
                nueve()
                base(tiempo,dato)
            elif x == '11111111':#8
                ocho()
                base(tiempo,dato)
            elif x == "11100000":#7
                siete()
                base(tiempo,3)
            elif x == "00111111":#6
                seis()
                base(tiempo,4)
            elif x == "10110111":#5
                cinco()
                base(tiempo,5)
            elif x == "01100111":#4
                cuatro()
                base(tiempo,6)
            elif x == "11110011":#3
                tres()
                base(tiempo,7)
            elif x == "11011010":#2
                dos()
                base(tiempo,8)
            elif x == "01100000":#1
                uno()
                base(tiempo,9)
            elif(x == "11111101"):#0
                cero()
                base(tiempo,10)
            elif(x == "Valor Fuera del Limite"):
                dato = 0
                nada()
                
    
    
    