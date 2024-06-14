widge = int(input("น้ำหนัก(กิโลกรัม):"))
high = int(input("ส่วนสูง(เซนติเมตร):"))

bmi = round(float(widge/((high/100) ** 2)),1)

print("BMI:",bmi)

if bmi < 18.5:
    print("น้ำหนักน้อย")
elif bmi >= 18.5 and bmi < 22.9:
    print("ปกติ(สุขภาพดี)")
elif bmi >= 23 and bmi < 24.9:
    print("ท้วม/โรคอ้วนระดับ 1")
elif bmi >= 25 and bmi < 29.9:
    print("อ้วน/โรคอ้วนระดับ 2")
elif bmi > 30:
    print("อ้วนมาก/โรคอ้วนระดับ 3")