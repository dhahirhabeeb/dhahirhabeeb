def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "خطأ: لا يمكن القسمة على صفر"
    return a / b

def calculator():
    print("=== آلة حاسبة بسيطة ===")
    print("العمليات المتاحة: + - * /")
    print("اكتب 'خروج' للإنهاء\n")

    while True:
        user_input = input("أدخل العملية الحسابية (مثال: 5 + 3): ").strip()

        if user_input == "خروج":
            print("وداعاً!")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("صيغة غير صحيحة. مثال: 5 + 3\n")
                continue

            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])

            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print(f"العملية '{op}' غير معروفة\n")
                continue

            print(f"النتيجة: {result}\n")

        except ValueError:
            print("خطأ: تأكد من إدخال أرقام صحيحة\n")

if __name__ == "__main__":
    calculator()
