# main function
def main():
    while True:
        print("\nUnit converter\n")
        print("1. Convert Length")
        print("2. Convert Weight")
        print("3. Convert Volume")
        print("4. Convert Temperature")
        print("5. Convert Time")
        print("6. Convert Speed")
        print("7. Exit the program\n")
        choice = input("What do you want to convert? ")
        print("")
        # prompting the user for input if he doesn't opt for any of the provided choices
        if choice.isdigit() and 1 <= int(choice) <= 7:
            choice = int(choice)
            break
        else:
            print("Please enter a valid number between 1 and 7.")
    # calling the function according to the user's choice
    if int(choice) == 1:
        print(length_converter(choice))
    elif int(choice) == 2:
        print(weight_converter(choice))
    elif int(choice) == 3:
        print(volume_converter(choice))
    elif int(choice) == 4:
        print(temp_converter(choice))
    elif int(choice) == 5:
        print(time_converter(choice))
    elif int(choice) == 6:
        print(speed_converter(choice))
    elif int(choice) == 7:
        print("Terminating the program.\n ")
        exit()
    convert_again = input("\nDo you want to run the program again? ").lower()
    while not convert_again.lower() == "yes" and not convert_again.lower() == "no":
        print("\nPlease type either 'yes' or 'no'")
        convert_again = input("\nDo you want to run the program again? ")
    if convert_again.lower() == "yes":
        main()
    else:
        print("\nGoodbye! See you again.\n")
        return
# defining length converter function
def length_converter(n):
    print("Length Converter is now active\n")
    print("1. Convert meter to km")
    print("2. Convert km to meter")
    print("3. Convert feet to meter")
    print("4. Convert meter to feet\n")
    opt = input("Select any one option: ")
    while not opt.isdigit() or 0<int(opt)>4:
        print("\nEnter the digit next to the desired option.\n ")
        opt = input("Select any one option: ")
    if int(opt) == 1:
        meter = input("\nEnter the length in meters: ")
        while not meter.replace('.', '', 1).isnumeric() or (meter.count('.') > 1):
            print("\nPlease enter the length in digits.\n ")
            meter = input("Enter the length in meters: ")
            print("")
        km = float(meter) / 1000
        return f"The length in kms is {'%.2f' % km} kms"
    elif int(opt) == 2:
        kms = input("\nEnter the length in kms: ")
        while not kms.replace('.', '', 1).isnumeric() or (kms.count('.') > 1):
            print("\nPlease enter the length in digits.\n ")
            kms = input("Enter the length in kms: ")
        meter2 = float(kms) * 1000
        return f"The length in meters is {'%.2f' % meter2} meters"
    elif int(opt) == 3:
        feet = input("\nEnter the length in feet: ")
        while not feet.replace('.', '', 1).isnumeric() or (feet.count('.') > 1):
            print("\nPlease enter the length in digits.\n ")
            feet = input("Enter the length in feet: ")
        meter3 = float(feet) * 3.28084
        return f"The length in meters is approximately { '%.2f' % meter3} meters"
    elif int(opt) == 4:
        meter4 = input("\nEnter the length in meters: ")
        while not meter4.replace('.', '', 1).isnumeric() or (meter4.count('.') > 1):
            print("\nPlease enter the length in digits.\n ")
            meter4 = input("Enter the length in meters: ")
        feet2 = float(meter4) * 0.3048
        return f"The length in feet is {'%.2f' % feet2} feet"
    else:
        return "Invalid input"

# defining weight converter function
def weight_converter(n):
    print("Weight Converter is now active\n")
    print("1. Convert kgs to pounds")
    print("2. Convert pounds to kgs")
    print("3. Convert kgs to grams")
    print("4. Convert pounds to grams\n")
    opt = input("Select any one option: ")
    while not opt.isdigit() or 0<int(opt)>4:
        print("\nEnter the digit next to the desired option.\n ")
        opt = input("Select any one option: ")
    if int(opt) == 1:
        kg = input("\nEnter the weight in kgs: ")
        while not kg.replace('.', '', 1).isnumeric() or (kg.count('.') > 1):
            print("\nPlease enter the weight in digits.\n ")
            kg = input("Enter the weight in kgs: ")
        pound = float(kg) * 2.20462
        return f"The weight in pounds is {'%.2f' % pound} pounds"
    elif int(opt) == 2:
        pound2 = input("\nEnter the weight in pounds: ")
        while not pound2.replace('.', '', 1).isnumeric() or (pound2.count('.') > 1):
            print("\nPlease enter the weight in digits.\n ")
            pound2 = input("Enter the weight in pounds: ")
        kg2 = float(pound2) * 0.453592
        return f"The weight in kgs is {'%.2f' % kg2} kgs"
    elif int(opt) == 3:
        kg3 = input("\nEnter the weight in kgs: ")
        while not kg3.replace('.', '', 1).isnumeric() or (kg3.count('.') > 1):
            print("\nPlease enter the weight in digits.\n ")
            kg3 = input("Enter the weight in kgs: ")
        grams = float(kg3) * 1000
        return f"The weight in grams is {grams} grams"
    elif int(opt) == 4:
        pound3 = input("\nEnter the weight in pounds: ")
        while not pound3.replace('.', '', 1).isnumeric() or (pound3.count('.') > 1):
            print("\nPlease enter the weight in digits.\n ")
            pound3 = input("Enter the weight in pounds: ")
        grams2 = float(pound3) * 453.592
        return f"The weight in grams is {'%.2f' % grams2} grams"
    else:
        return "Invalid input"

# defining volume converter function
def volume_converter(n):
    print("Volume Converter is now active\n")
    print("1. Convert Milliliters to Liters")
    print("2. Convert Liters to Milliliters")
    print("3. Convert Gallons to Liters")
    print("4. Convert Liters to Gallons\n")
    opt = input("Select any one option: ")
    while not opt.isdigit() or 0<int(opt)>4:
        print("\nEnter the digit next to the desired option.\n ")
        opt = input("Select any one option: ")
    if int(opt) == 1:
        ml = input("\nEnter the volume in Milliliters: ")
        while not ml.replace('.', '', 1).isnumeric() or (ml.count('.') > 1):
            print("\nPlease enter the volume in digits.\n ")
            ml = input("Enter the volume in Milliliters: ")
        l1 = float(ml) / 1000
        return f"The volume in liters is {'%.2f' % l1} liters"
    elif int(opt) == 2:
        l2 = input("\nEnter the volume in liters: ")
        while not l2.replace('.', '', 1).isnumeric() or (l2.count('.') > 1):
            print("\nPlease enter the volume in digits.\n ")
            l2 = input("Enter the volume in liters: ")
        ml2 = float(l2) * 1000
        return f"The volume in Milliliters is {'%.2f' % ml2} Milliliters"
    elif int(opt) == 3:
        gal = input("\nEnter the volume in Gallons: ")
        while not gal.replace('.', '', 1).isnumeric() or (gal.count('.') > 1):
            print("\nPlease enter the volume in digits.\n ")
            gal = input("Enter the volume in Gallons: ")
        l3 = float(gal) * 3.78541
        return f"The volume in liters is {'%.2f' % l3} liters"
    elif int(opt) == 4:
        l4 = input("\nEnter the volume in liters: ")
        while not l4.replace('.', '', 1).isnumeric() or (l4.count('.') > 1):
            print("\nPlease enter the volume in digits.\n ")
            l4 = input("Enter the volume in liters: ")
        gal2 = float(l4) / 3.78541
        return f"The volume in Gallons is {'%.2f' % gal2} Gallons"
    else:
        return "Invalid input"

# defining temperature converter function
def temp_converter(n):
    print("Temperature Converter is now active\n")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Convert Celsius to Kelvin")
    print("4. Convert Kelvin to Celsius\n")
    opt = input("Select any one option: ")
    while not opt.isdigit() or 0<int(opt)>4:
        print("\nEnter the digit next to the desired option.\n ")
        opt = input("Select any one option: ")
    if int(opt) == 1:
        cel = input("\nEnter the temperature in Celsius: ")
        while not cel.replace('.', '', 1).isnumeric() or (cel.count('.') > 1):
            print("\nPlease enter the volume in digits.\n ")
            cel = input("Enter the temperature in Celsius: ")
        fah = (float(cel) * 9 / 5) + 32
        return f"The temperature in Fahrenheit is {'%.2f' % fah} degrees"
    elif int(opt) == 2:
        fah2 = input("\nEnter the temperature in Fahrenheit: ")
        while not fah2.replace('.', '', 1).isnumeric() or (fah2.count('.') > 1):
            print("\nPlease enter the volume in digits.\n ")
            fah2 = input("Enter the temperature in Fahrenheit: ")
        cel2 = (float(fah2) - 32) * 5 / 9
        return f"The temperature in Celsius is {'%.2f' % cel2} degrees"
    elif int(opt) == 3:
        cel3 = input("\nEnter the temperature in Celsius: ")
        while not cel3.replace('.', '', 1).isnumeric() or (cel3.count('.') > 1):
            print("\nPlease enter the volume in digits.\n ")
            cel3 = input("Enter the temperature in Celsius: ")
        kel = float(cel3) + 273.15
        return f"The temperature in Kelvin is {'%.2f' % kel} degrees"
    elif int(opt) == 4:
        kel2 = input("\nEnter the temperature in Kelvin: ")
        while not kel2.replace('.', '', 1).isnumeric() or (kel2.count('.') > 1):
            print("\nPlease enter the volume in digits.\n ")
            kel2 = input("Enter the temperature in Kelvin: ")
        cel4 = float(kel2) - 273.15
        return f"The temperature in Celsius is {'%.2f' % cel4} degrees"
    else:
        return "Invalid input"

# defining time converter function
def time_converter(n):
    print("Time Converter is now active\n")
    print("1. Convert Seconds to Minutes")
    print("2. Convert Minutes to Hours")
    print("3. Convert Hours to Days")
    print("4. Convert Days to Weeks\n")
    opt = input("Select any one option: ")
    while not opt.isdigit() or 0<int(opt)>4:
        print("\nEnter the digit next to the desired option.\n ")
        opt = input("Select any one option: ")
    if int(opt) == 1:
        sec = input("\nEnter the time in Seconds: ")
        while not sec.replace('.', '', 1).isnumeric() or (sec.count('.') > 1):
            print("\nPlease enter the time in digits.\n ")
            sec = input("Enter the time in Seconds: ")
        mins = float(sec) / 60
        return f"The time in Minutes is {'%.2f' % mins} minutes"
    elif int(opt) == 2:
        mins2 = input("\nEnter the time in Minutes: ")
        while not mins2.replace('.', '', 1).isnumeric() or (mins2.count('.') > 1):
            print("\nPlease enter the time in digits.\n ")
            mins2 = input("Enter the time in Minutes: ")
        hrs = float(mins2) / 60
        return f"The time in Hours is {'%.2f' % hrs} hours"
    elif int(opt) == 3:
        hrs2 = input("\nEnter the time in Hours: ")
        while not hrs2.replace('.', '', 1).isnumeric() or (hrs2.count('.') > 1):
            print("\nPlease enter the time in digits.\n ")
            hrs2 = input("Enter the time in Hours: ")
        days = float(hrs2) / 24
        return f"The time in Days is {'%.2f' % days} days"
    elif int(opt) == 4:
        days2 = input("\nEnter the time in Days: ")
        while not days2.replace('.', '', 1).isnumeric() or (days2.count('.') > 1):
            print("\nPlease enter the time in digits.\n ")
            days2 = input("Enter the time in Days: ")
        week = float(days2) / 7
        return f"The time in Weeks is {'%.2f' % week} weeks"
    else:
        return "Invalid input"

# defining speed converter function
def speed_converter(n):
    print("Speed Converter is now active\n")
    print("1. Convert Kilometers per Hour (km/h) to Miles per Hour (mph)")
    print("2. Convert Miles per Hour (mph) to Kilometers per Hour (km/h)")
    print("3. Convert Kilometers per Hour (km/h) to Meters per Second (m/s)")
    print("4. Convert Meters per Second (m/s) to Kilometers per Hour (km/h)\n")

    opt = input("Select any one option: ")
    while not opt.isdigit() or not (1 <= int(opt) <= 4):
        print("\nEnter a valid option (1, 2, 3, or 4).\n")
        opt = input("Select any one option: ")

    if int(opt) == 1:
        while True:
            kmh = input("\nEnter the speed in Kilometers per Hour (km/h) in the format 'value1/value2': ")
            km, hr = kmh.split("/")
            if km.replace('.', '', 1).isnumeric() and hr.replace('.', '', 1).isnumeric():
                real_km = float(km) / float(hr)
                mile = real_km * 0.621371
                return f"The speed in Miles per Hour (mph) is {'%.2f' % mile} miles per hour"
            else:
                print("Invalid input. Please enter valid numeric values separated by '/'.")
    elif int(opt) == 2:
        while True:
            mile2 = input("\nEnter the speed in Miles per Hour (mph) in the format 'value1/value2': ")
            mile3, hr2 = mile2.split("/")
            if mile3.replace('.', '', 1).isnumeric() and hr2.replace('.', '', 1).isnumeric():
                real_mile = float(mile3) / float(hr2)
                km2 = real_mile * 1.60934
                return f"The speed in Kilometers per Hour (km/h) is {'%.2f' % km2} Kilometers per hour"
            else:
                print("Invalid input. Please enter valid numeric values separated by '/'.")
    elif int(opt) == 3:
        while True:
            kmh2 = input("\nEnter the speed in Kilometers per Hour (km/h) in the format 'value1/value2': ")
            km3, hr3 = kmh2.split("/")
            if km3.replace('.', '', 1).isnumeric() and hr3.replace('.', '', 1).isnumeric():
                real_km2 = float(km3) / float(hr3)
                meter = (real_km2 * 1000) / 3600
                return f"The speed in Meters per Second (m/s) is {'%.2f' % meter} meters per second"
            else:
                print("Invalid input. Please enter valid numeric values separated by '/'.")
    elif int(opt) == 4:
        while True:
            ms = input("\nEnter the speed in Meters per Second (m/s) in the format 'value1/value2': ")
            meter2, sec = ms.split("/")
            if meter2.replace('.', '', 1).isnumeric() and sec.replace('.', '', 1).isnumeric():
                real_meter = float(meter2) / float(sec)
                km4 = real_meter * 3.6
                return f"The speed in Kilometers per Hour (km/h) is {'%.2f' % km4} km per hour"
            else:
                print("Invalid input. Please enter valid numeric values separated by '/'.")

if __name__ == "__main__":
    main()
