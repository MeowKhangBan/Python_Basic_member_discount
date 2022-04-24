import time
print('-------------------- \nลงทะเบียนคอร์ส online \n--------------------')
time.sleep(0.5)
customer_list = {'gura':'gura@gmail.com','ame':'ame@gmail.com','Aqua':'aqua@gmail.com'
                ,'pekora':'pekora@gmail.com','kona':'kona@gmail.com','hongfei':'hongfei@gmail.com'}

def old_or_new_customer(price = 990):
    print('--------------------')
    prereg = str(input('คุณเคยสมัครคอร์สเรียนของเรามาก่อนหรือไม่ y/n : '))
    if prereg == 'y':
        print('--------------------')
        print('หากคุณเคยสมัครคอร์สของเรามาก่อนแล้ว')
        print('--------------------')
        time.sleep(1)
        print('กรุณากรอกข้อมูลเพื่อยืนยันตัวตน')
        name_auth1 = str(input('Name :'))
        email_auth1 = str(input('Email :'))
        print('--------------------')
        if name_auth1.lower() in customer_list and email_auth1.lower() == customer_list[name_auth1.lower()]:
            print('คุณได้รับส่วนลดสำหรับการสมัครคอร์สเรียน 20%')
            time.sleep(1)
            print('--------------------')
            print(f'''ค่าคอร์สเรียน {(price*80)/100} บาท สามารถขำระเงินได้ที่
            SCB : XXX-XXXXXX-X
            Promtpay : XXX-XXXXXXX''')
            print('--------------------')
            time.sleep(0.5)
            print('ขอบคุณที่ใช้บริการ')
        else:
            print('ไม่พบข้อมูล')
    else:
        print('กรุณากรอกข้อมูลเพื่อใช้ในการสมัครเรียน')
        name_firstreg = str(input('Name :'))
        email_firstreg = str(input('Email :'))
        customer_list[f'{name_firstreg.lower()}'] = f'{email_firstreg.lower()}'
        time.sleep(1)
        print('--------------------')
        print(f'''ค่าคอร์สเรียน {price} บาท สามารถขำระเงินได้ที่
                SCB : XXX-XXXXXX-X
                Promtpay : XXX-XXXXXXX''')
        print('--------------------')
        time.sleep(0.5)
        print('ขอบคุณที่ใช้บริการ')
            
while True:
    print('''กรุณาเลือกคอร์สเรียน 
    A.ยกระดับจากนินจาธรรมดาสู่โฮคาเงะสไตล์นารูโตะ -990 Baht
    B.เขียน Python จาก 0 โดยไม่ต้องเรียน -990 Baht
    C.ทำอาหารระดับเทพโดยเชฟโคมัตสึ -1990 Baht
    D.เรียนรู้สู่การเป็นโจรชื่อดังระดับโลก -1 Baht
    
    N.ฉันไม่ต้องการเรียนคอร์สเหล่านี้ ''')
    time.sleep(1)
    answer = str(input('กรุณาเลือกคอร์สโดยพิมตัวอักษรพิมใหญ่ :'))
    time.sleep(1)
    if answer == 'A':
        old_or_new_customer(990)
        break
    elif answer == 'B':
        old_or_new_customer(990)
        break
    elif answer == 'C':
        old_or_new_customer(1990)
        break
    elif answer == 'D':
        old_or_new_customer(1)
        break
    elif answer == 'N':
        break
    elif answer != 'A' or 'B' or 'C' or 'D':
        print('กรุณากรอกตัวอักษรคอร์สเรียนให้ถูกต้อง')
        print('--------------------')