import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports

#ports = serial.tools.list_ports.comports()
#for port, desc, hwid in sorted(ports):
    #print("{}: {} [{}]".format(port, desc, hwid))

ser = serial.Serial("COM2", 9600)
#print(ser.readline())

#print(htr1)
#print(a)
res = 1
i = 0
time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)


##print(temp)

##print(Humidity)


##print(Flame)


##print(a[3])
##print(Smoke)
while res:
    #cc = str(1234)
    #print(cc)
    #val = cc
    firebase1 = firebase.FirebaseApplication('https://forest-fire-monitering-s-27358-default-rtdb.firebaseio.com/', None)

    for i in range(0, 4):
        #string1 = "123"
        #string1=str(ser.readline())
        #string1=string1[1:][:0]
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        temp = a[0]
        temp = temp[4:]
        data = {'date': datetime.now().strftime("%Y-%m-%d"),
                'reading': temp,
                'time': datetime.now().strftime("%H:%M")
                }
        result = firebase1.patch(
            'https://forest-fire-monitering-s-27358-default-rtdb.firebaseio.com//' + '/Temperature_data/' + str(i), data)
        print(result)

    for i in range(0, 4):
        #string2 = "123"
        string2=str(ser.readline())
        #string2=string2[1:][:0]
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        Humidity = a[1]
        Humidity = Humidity[4:]
        data1 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': Humidity,
                 'time': datetime.now().strftime("%H:%M")
                 }
        result1 = firebase1.patch('https://forest-fire-monitering-s-27358-default-rtdb.firebaseio.com/' + '/Humidity_data/' + str(i),
                                  data1)
        print(result1)

        for i in range(0, 4):
            # string2 = "123"
            string3 = str(ser.readline())
            # string2=string2[1:][:0]
            a = []
            htr1 = str(ser.readline())
            a = htr1.split(",")
            Flame = a[2]
            Flame = Flame[4:]
            data2 = {'date': datetime.now().strftime("%Y-%m-%d"),
                     'reading': Flame,
                     'time': datetime.now().strftime("%H:%M")
                     }
            result2 = firebase1.patch(
                'https://forest-fire-monitering-s-27358-default-rtdb.firebaseio.com/' + '/Flamesensor_data/' + str(i),
                data2)
            print(result2)

            for i in range(0, 4):
                # string2 = "123"
                string4 = str(ser.readline())
                # string2=string2[1:][:0]
                a = []
                htr1 = str(ser.readline())
                a = htr1.split(",")
                Smoke = a[3]
                Smoke = Smoke[4:][:-5]
                data3 = {'date': datetime.now().strftime("%Y-%m-%d"),
                         'reading': Smoke,
                         'time': datetime.now().strftime("%H:%M")
                         }
                result3 = firebase1.patch(
                    'https://forest-fire-monitering-s-27358-default-rtdb.firebaseio.com/' + '/Smokesensor_data/' + str(i),
                    data3)
                print(result3)


    res = 0
