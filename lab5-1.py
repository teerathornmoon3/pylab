def reg(w,l):
    return w*l

try:
    w = float(input("ความกว้างของสี่เหลี่ยม: "))
    l = float(input("ความยาวของสี่เหลี่ยม: "))
    print(f"พท. สี่เหลียมกว้าง {w} ยาว {l} คือ",reg(w,l))
except Exception as e:
    print("Error:",e)
