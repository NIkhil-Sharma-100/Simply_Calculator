from sympy import sympify,sin,cos,tan,cot,sec,log,pi

def calculator(expr):
    try:
        result = sympify(expr).evalf(3)     # now sympy will execute mathematical operations andn round it to 2 decimal place
        print("Result : ",result)
    except Exception as e:
        print("Exception",e)    

print("🧮 CALCULATOR")
while True:
    expr = input("Enter Your Expression: ")
    calculator(expr)

  
