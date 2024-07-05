def BMI(w,h):
    return round(w/((h/100)**2),2)

def StatusCheck(bmi):
    res = None
    if bmi < 18.5:
        res = "น้ำหนักน้อย"
    elif bmi >= 18.5 and bmi < 22.9:
        res = "ปกติ(สุขภาพดี)"
    elif bmi >= 23 and bmi < 24.9:
        res = "ท้วม/โรคอ้วนระดับ 1"
    elif bmi >= 25 and bmi < 29.9:
        res = "อ้วน/โรคอ้วนระดับ 2"
    elif bmi > 30:
        res = "อ้วนมาก/โรคอ้วนระดับ 3"
    
    if res:
        return res
    else:
        print("BMI Chect Error:Can't check BMI(%d)" %res)
        return

try:
    H = float(input("หา BMI : ส่วนสูง(cm) = "))
    W = float(input("หา BMI : น้ำหนัก(kg) = "))
    print(f"ความสูง {H} cm น้ำหนัก {W} kg มีค่า BMI คือ {BMI(W, H)} ซึ่งอยู่ในเกณฑ์: {StatusCheck(BMI(W, H))}")
except Exception as e:
    print("Error:",e)