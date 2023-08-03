# สร้างฟังก์ชัน hello(name) รับค่า name
def hello(name="no name", age=0):
    print(f"Hello {name} Your age is {age}")


# เรียกใช้งานฟังก์ชัน hello(name)
hello("Samit", 30)
hello("Wichai", 40)
hello("Somjai", 25)
hello()
# สร้างฟังก์ชันทีมีการ return


def area(width, height):
    return width * height


# เรียกใช้งานฟังก์ชัน area()
print("Area is ", area(10, 20))


# สร้างฟังก์ชันเช็คเบอร์มงคล
def berdee(phone_number):

    total = 0
    if len(phone_number) == 10:
        # หาผลรวมเบอร์โทรศัพท์
        for n in phone_number:
            total = total + int(n)
        return total
    elif len(phone_number) > 10:
        return 'ป้อนเบอร์เกิน'
    elif len(phone_number) < 10:
        return 'ป้อนเบอร์ไม่ครบ 10 หลัก'
    else:
        return 'รูปแบบเบอร์ไม่ถูกต้อง'


# เรียกใช้งานเช็คเบอร์มงคล
phone = input('Enter phone nubmer:')
print(berdee(phone))
