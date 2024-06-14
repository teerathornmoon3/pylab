widge = int(input("น้ำหนัก(กิโลกรัม):"))
high = int(input("ส่วนสูง(เซนติเมตร):"))

bmi = widge/((high/100) ** 2)

print(bmi.2f)

if bmi < 18.50:
    print()