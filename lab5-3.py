def Tprice(pcount):
    total = float(0)
    for i in range(pcount):
        try:
            total += float(input(f"ราคาสินค้าชิ้นที่ {i+1}: "))
        except Exception as Total_e:
            print("Error:",Total_e)
    return round(total,2)


def discountF(price,persent):
    return round((price*persent)/100,2)

def taxF(price):
    return round(float((price*7)/100),2)

def totalF(p_total,tax,discount):
    return round(float((p_total-discount)+tax),2)

try:
    p_count = int(input("จำนวนสินค้า: "))
    t_price = Tprice(p_count)
    discount = discountF(t_price,5)
    tax = taxF(t_price - discount)
    
    print(f"ราคารวมของสินค้าคือ {t_price} บาท มีภาษีจำนวน {tax} บาท และส่วนลด {discount} บาท รวมเป็น {totalF(t_price,tax,discount)} บาท")
except Exception as e:
    print("Error:",e)
