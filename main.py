from machine import Pin, PWM
from time import sleep

# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# Tehot (itselle muistiin)
# 25% = 16383
# 50% = 32767
# 75% = 49181
# 100% = 65535

# Funktiot:

# Renkaiden pyörimissuunta eteenpäin
def pyoriEteen():
    m1.value(1)
    m2.value(1)

# Renkaiden pyörimissuunta taaksepäin
def pyoriTaakse():
    m1.value(0)
    m2.value(0)

# Liikuttaa FoCaria
# Oletusarvot 75%, 2s
def eteenpain(nopeus = 49181, aika = 2):
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

# Kääntää FoCarin vasemmalle
def vasen():
    m1.value(1)
    m2.value(0)
    e1.duty_u16(27500)
    e2.duty_u16(27500)
    sleep(1)

# Kääntää FoCarin oikealle
def oikea():
    m1.value(0)
    m2.value(1)
    e1.duty_u16(27500)
    e2.duty_u16(27500)
    sleep(1)

# Tauko, oletusarvo 1s
def tauko(aika = 1):
    sleep(aika)

# Pysäyttää FoCarin
def pysayta():
    e1.duty_u16(0)
    e2.duty_u16(0)

# Käännä FoCar 180°
def ympari():
    m1.value(0)
    m2.value(1)
    e1.duty_u16(49181)
    e2.duty_u16(49181)
    sleep(1)

# 5 sekunnin tauko (ehtii laskemaan FoCar lattialle)
sleep(5)

# Määritellään renkaiden pyörimissuunta eteenpäin
pyoriEteen()

# Liikutaan suoraan eteenpäin n. puoli metriä
eteenpain()

# Pysäytetään FoCar
# 1 sekunnin jälkeen käännytään oikealle n. 90° ja liikutaan eteenpäin n. puoli metriä
# Oikealle käännyttäessä renkaiden pyörimissuunnat ja nopeus määritellään uusiksi
pysayta()

tauko()

oikea()

# Pysäytetään FoCar, määritellään renkaiden pyörimissuunta eteenpäin
# 1 sekunnin jälkeen liikutaan suoraan eteenpäin n. puoli metriä
pysayta()

tauko()

pyoriEteen()

eteenpain()

# Pysäytetään FoCar
# 1 sekunnin jälkeen käännytään oikealle n. 90° ja liikutaan eteenpäin n. puoli metriä
pysayta()

tauko()

oikea()