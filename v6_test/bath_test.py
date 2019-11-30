import RPi.GPIO as GPIO
from datetime import datetime
import pymysql
from multiprocessing import Process
import time
'''
set model
'''
GPIO.setmode(GPIO.BOARD)

'''
============================================================================================
monitor Sensor Data channel
use GPIO.0-----> Port 11 as the infrared sensor1 data channel   In side
use GPIO.1-----> Port 12 as the infrared sensor2 data channel   Out side

Data stream state:
    1 --------------> Work Normally 
    0 --------------> Something Shelter from the sensor

So the common state is 3.3V high vol
keep the port volume stable and strict the electric stream 
Use PUD_UP to pull up resistence on the port

--------------------------------------------------------|
Note!                                                   |
Use Port 6 on Raspberry to link the shared  Ground      |
--------------------------------------------------------|        

=============================================================================================
'''
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)

'''
--------------------------------------------
Use GPIO.13------> Port 13 as the led      |
--------------------------------------------
'''


'''
start connect to mysql
'''
conn = pymysql.connect(
            host = '192.168.0.103',
            user = 'root',
            password = '12345',
            db = 'v6_db',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )
cursor = conn.cursor()


'the sum number of the people'
sum_people = 0

'''
start the monitor
'''

try:
    while True:
        'Come in situation'
        if GPIO.input(11) == 0:
            print('Waiting here1')
            while GPIO.input(12) == 1:
                pass

            while GPIO.input(11) == 0:
                pass
            
            print('Come in')
            sum_people += 1
            print(sum_people)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            insert_sql = """INSERT INTO 
                            bath_tbl(sum_people,  time) 
                            values('%d', '%s')""" % (sum_people, now)
            cursor.execute(insert_sql)
            conn.commit()
            while GPIO.input(12) == 0:
                pass
        'Out situation'
        if GPIO.input(12) == 0:
            print('Wating here 2')
            while GPIO.input(11) == 1:
                pass

            while GPIO.input(12) == 0:
                pass

            print('get out')
            sum_people -= 1
            if sum_people <= 0:
                sum_people = 0
            print(sum_people)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            insert_sql = """INSERT INTO
                        bath_tbl(sum_people, time) 
                        VALUES('%d', '%s')""" % (sum_people, now)
            cursor.execute(insert_sql)
            conn.commit()
            while GPIO.input(11) == 0:
                pass
except (BaseException), ex:
    print(ex)
    GPIO.cleanup()
    print('GPIO has been clean up port...')
finally:
    print('close sql service cursor and connection...')
    cursor.close()
    conn.close()


