wmax = 20
amax = 10
tmax = 20

def midscore(w, a, t):
    if w>wmax or a>amax or t>tmax:
        return [0,f"มีค่าคะแนนที่เกินค่าสูงสุด!"]
    else:
        return [1,f"บันทึกคะแนนเรียบร้อย\n\tคะแนนเก็บ {w} คะแนน\n\tคะแนนจิตพิสัย {a} คะแนน\n\tคะแนนสอบ {t} คะแนน\n\tรวม {w+a+t} คะแนน"]
        

try:        
    w = int(input(f"คะแนนเก็บ(Max:{wmax}): "))
    a = int(input(f"คะแนนจิตพิสัย(Max:{amax}): "))
    t = int(input(f"คะแนนสอบ(Max:{tmax}): "))
    
    if midscore(w,a,t)[0] == 1:
        print("Success:",midscore(w,a,t)[1])
    else:
        print("Error:",midscore(w,a,t)[1])
    
except Exception as e:
    print("Error:",e)
    
    