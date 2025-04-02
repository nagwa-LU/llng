#python calculator
#سنطلب من المستخدم ادخال كلا من الرقم الاول بعدها نوع العمليه الحسابيه وبعدها الرقم الثاني
#واخيرا نظهر النتيجه
#let's Gooo
num1 = int(input("Enter frist number : "))
type_operation = input("Enter operation type (+ - / *) : ")
num2 = int(input("Enter second number : "))
if type_operation == '+':
    result = num1 + num2
    print(result)
elif type_operation == '-':
    result = num1 - num2
    print(result)
elif type_operation == '/':
    result = num1/num2
    print(result)
elif type_operation == '*':
    result = num1*num2
    print(result)

    

         


