def menu():
    print("Welcome to BMI calculator")
    print("1.Metric calculation\n2.Imperial calculation")
    choice=int(input("Enter your choice of calculation: "))
    user_input(choice)

def user_input(choice):
    global height
    global weight
    if choice == 1:
        height = float(input("Enter the height of the person: "))
        weight = float(input("Enter the weight of the person: "))
        metric_calc(height,weight)
    elif choice == 2:
        height = float(input("Enter the height of the person: "))
        weight = float(input("Enter the weight of the person: "))
        imperial_calc(height,weight)
    else:
        menu()

def metric_calc(x,y):
    print("---------------------")
    print("Metric calculation")
    result=y/(x**2)*10000
    print(f"Your BMI in metric :{result}")
    if result < 18.5:
        print("Under weight")
    elif result>18.5 and result<=24.9:
        print("Normal")
    elif result>24.9 and result<=29.9:
        print("Over weight")
    elif result>29.9 and result<=34.9:
        print("Obesity class-I")
    elif result>34.9 and result<=39.9:
        print("Obesity class-II")
    elif result>40:
        print("extreme obisity")
    else:
        pass

def imperial_calc(x,y):
    print("---------------------")
    print("Imperial calculation")
    result_imperial=(y/x**2)*703*10000
    print(f"Your BMI in imperial : {result_imperial}")
    if result_imperial < 18.5:
        print("Under weight")
    elif result_imperial>18.5 and result_imperial<=24.9:
        print("Normal")
    elif result_imperial>24.9 and result_imperial<=29.9:
        print("Over weight")
    elif result_imperial>29.9 and result_imperial<=34.9:
        print("Obesity class-I")
    elif result_imperial>34.9 and result_imperial<=39.9:
        print("Obesity class-II")
    elif result_imperial>40:
        print("extreme obisity")
    else:
        pass

menu()