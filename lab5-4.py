def F(c):
    return float(((9*c)/5)+32)

def K(c):
    return float(c+273.15)

try:
    celcius = float(input("อุณหภูมิ(องศาเซลเซียส):"))
    print(f"แปลงเป็นองศาฟาเรนไฮด์ได้ {F(celcius)} องศา และแปลงเป็นองศาเควินได้ {K(celcius)} องศา")
except Exception as e:
    print("Error:",e)