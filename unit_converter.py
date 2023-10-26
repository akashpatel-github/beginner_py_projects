#main function
def main():
    while True:
        print("")
        print("Unit converter")
        print("")
        print("1. Convert Length")
        print("2. Convert Weight")
        print("3. Convert Volume")
        print("4. Convert Temperature")
        print("5. Convert Time")
        print("6. Convert Speed")
        print("7. Exit the program")
        print("")
        choice = input("What do you want to convert? ")
        print("")
        #prompting the user for input if he doesn't opt for any of the provided choices
        if choice.isdigit() and 1 <= int(choice) <= 7:
            choice = int(choice)
            break
        else:
            print("Please enter a valid number between 1 and 7.")
    #calling the function according to the user's choice
    if int(choice) == 1:
        print("")
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
        print("Terminating the program. ")
        print("")
        exit()

#defining length converter function
def length_converter(n):
    print("Length Converter is now active")
    print("")
    print("1. Convert meter to km")
    print("2. Convert km to meter")
    print("3. Convert feet to meter")
    print("4. Convert meter to feet")
    print("")
    opt = input("Select any one option: ")
    print("")
    while opt.isalpha():
        opt = input("Select any one option: ")
        print("")
    if int(opt) == 1:
        meter = input("Enter the length in meters ")
        while meter.isalpha():
            print("Please enter the length in digits ")
            meter = input("Enter the length in meters: ")
        km = float(meter) / 1000
        return f"The length in kms is {km} kms"
    elif int(opt) == 2:
        kms = input("Enter the length in kms: ")
        while kms.isalpha():
            print("Please enter the length in digits ")
            kms = input("Enter the length in kms: ")
        meter2 = float(kms) * 1000
        return f"The length in meters is {'%.2f' % meter2} meters"
    elif int(opt) == 3:
        feet = input("Enter the length in feet: ")
        while feet.isalpha():
            print("Please enter the length in digits ")
            feet = input("Enter the length in feet: ")
        meter3 = float(feet) * 3.28084
        return f"The length in meters is approximately { '%.2f' % meter3} meters"
    elif int(opt) == 4:
        meter4 = input("Enter the length in meters: ")
        while meter4.isalpha():
            print("Please enter the length in digits ")
            meter4 = input("Enter the length in meters: ")
        feet2 = float(meter4) * 0.3048
        return f"The length in feet is {'%.2f' % feet2} feet"
    else:
        return "Invalid input"

#defining weight converter function
def weight_converter(n):
    print("Weight Converter is now active")
    print("1. Convert kgs to pounds")
    print("2. Convert pounds to kgs")
    print("3. Convert kgs to grams")
    print("4. Convert pounds to grams")
    opt = input("Select any one option: ")
    while opt.isalpha():
        opt = input("Select any one option: ")
    if int(opt) == 1:
        kg = input("Enter the weight in kgs: ")
        while kg.isalpha():
            print("Please enter the weight in digits ")
            kg = input("Enter the weight in kgs: ")
        pound = float(kg) * 2.20462
        return f"The weight in pounds is {'%.2f' % pound} pounds"
    elif int(opt) == 2:
        pound2 = input("Enter the weight in pounds: ")
        while pound2.isalpha():
            print("Please enter the weight in digits ")
            pound2 = input("Enter the weight in pounds: ")
        kg2 = float(pound2) * 0.453592
        return f"The weight in kgs is {'%.2f' % kg2} kgs"
    elif int(opt) == 3:
        kg3 = input("Enter the weight in kgs: ")
        while kg3.isalpha():
            print("Please enter the weight in digits ")
            kg3 = input("Enter the weight in kgs: ")
        grams = float(kg3) * 1000
        return f"The weight in grams is {grams} grams"
    elif int(opt) == 4:
        pound3 = input("Enter the weight in pounds: ")
        while pound3.isalpha():
            print("Please enter the weight in digits ")
            pound3 = input("Enter the weight in pounds: ")
        grams2 = float(pound3) * 453.592
        return f"The weight in grams is {'%.2f' % grams2} grams"
    else:
        return "Invalid input"

#defining volume converter function
def volume_converter(n):
    print("Volume Converter is now active")
    print("1. Convert Milliliters to Liters")
    print("2. Convert Liters to Milliliters")
    print("3. Convert Gallons to Liters")
    print("4. Convert Liters to Gallons")
    opt = input("Select any one option: ")
    while opt.isalpha():
        opt = input("Select any one option: ")
    if int(opt) == 1:
        ml = input("Enter the volume in Milliliters: ")
        while ml.isalpha():
            print("Please enter the volume in digits ")
            ml = input("Enter the volume in Milliliters: ")
        l1 = float(ml) / 1000
        return f"The volume in liters is {l1} liters"
    elif int(opt) == 2:
        l2 = input("Enter the volume in liters: ")
        while l2.isalpha():
            print("Please enter the volume in digits ")
            pound2 = input("Enter the volume in liters: ")
        ml2 = float(l2) * 1000
        return f"The volume in Milliliters is {ml2} Milliliters"
    elif int(opt) == 3:
        gal = input("Enter the volume in Gallons: ")
        while gal.isalpha():
            print("Please enter the volume in digits ")
            gal = input("Enter the volume in Gallons: ")
        l3 = float(gal) * 3.78541
        return f"The volume in liters is {'%.2f' % l3} liters"
    elif int(opt) == 4:
        l4 = input("Enter the volume in liters: ")
        while l4.isalpha():
            print("Please enter the volume in digits ")
            l4 = input("Enter the volume in liters: ")
        gal2 = float(l4) / 3.78541
        return f"The volume in Gallons is {'%.2f' % gal2} Gallons"
    else:
        return "Invalid input"

#defining temperature converter function
def temp_converter(n):
    print("Temperature Converter is now active")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Convert Celsius to Kelvin")
    print("4. Convert Kelvin to Celsius")
    opt = input("Select any one option: ")
    while opt.isalpha():
        opt = input("Select any one option: ")
    if int(opt) == 1:
        cel = input("Enter the temperature in Celsius: ")
        while cel.isalpha():
            print("Please enter the temperature in digits ")
            cel = input("Enter the temperature in Celsius: ")
        fah = (float(cel) * 9 / 5) / 1000
        return f"The temperature in Fahrenheit is {'%.2f' % fah} degrees"
    elif int(opt) == 2:
        fah2 = input("Enter the temperature in Fahrenheit: ")
        while fah2.isalpha():
            print("Please enter the temperature in digits ")
            fah2 = input("Enter the temperature in Fahrenheit: ")
        cel2 = (float(fah2) - 32) * 5 / 9
        return f"The temperature in Celsius is {'%.2f' % cel2} degrees"
    elif int(opt) == 3:
        cel3 = input("Enter the temperature in Celsius: ")
        while cel3.isalpha():
            print("Please enter the temperature in digits ")
            cel3 = input("Enter the temperature in Celsius: ")
        kel = float(cel3) + 273.15
        return f"The temperature in Kelvin is {'%.2f' % kel} degrees"
    elif int(opt) == 4:
        kel2 = input("Enter the temperature in Kelvin: ")
        while kel2.isalpha():
            print("Please enter the temperature in digits ")
            kel2 = input("Enter the temperature in Kelvin: ")
        cel4 = float(kel2) - 273.15
        return f"The temperature in Celsius is {'%.2f' % cel4} degrees"
    else:
        return "Invalid input"

#defining time converter function
def time_converter(n):
    print("Time Converter is now active")
    print("1. Convert Seconds to Minutes")
    print("2. Convert Minutes to Hours")
    print("3. Convert Hours to Days")
    print("4. Convert Days to Weeks")
    opt = input("Select any one option: ")
    while opt.isalpha():
        opt = input("Select any one option: ")
    if int(opt) == 1:
        sec = input("Enter the time in Seconds: ")
        while sec.isalpha():
            print("Please enter the time in digits ")
            sec = input("Enter the time in Seconds: ")
        mins = float(sec) / 60
        return f"The time in Minutes is {'%.2f' % mins} minutes"
    elif int(opt) == 2:
        mins2 = input("Enter the time in Minutes: ")
        while mins2.isalpha():
            print("Please enter the time in digits ")
            mns2 = input("Enter the time in Minutes: ")
        hrs = float(mins2) / 60
        return f"The time in Hours is {'%.2f' % hrs} hours"
    elif int(opt) == 3:
        hrs2 = input("Enter the time in Hours: ")
        while hrs2.isalpha():
            print("Please enter the time in digits ")
            hrs2 = input("Enter the time in Hours: ")
        days = float(hrs2) / 24
        return f"The time in Days is {'%.2f' % days} days"
    elif int(opt) == 4:
        days2 = input("Enter the time in Days: ")
        while days2.isalpha():
            print("Please enter the time in digits ")
            days2 = input("Enter the time in Days: ")
        week = float(days2) / 7
        return f"The time in Weeks is {'%.2f' % week} weeks"
    else:
        return "Invalid input"

#defining speed converter function
def speed_converter(n):
    print("Speed Converter is now active")
    print("1. Convert Kilometers per Hour (km/h) to Miles per Hour (mph)")
    print("2. Convert Miles per Hour (mph) to Kilometers per Hour (km/h)")
    print("3. Convert Kilometers per Hour (km/h) to Meters per Second (m/s)")
    print("4. Convert Meters per Second (m/s) to Kilometers per Hour (km/h)")
    opt = input("Select any one option: ")
    while opt.isalpha():
        opt = input("Select any one option: ")
    if int(opt) == 1:
        kmh = input("Enter the speed in Kilometers per Hour (km/h): ")
        while "/" not in kmh:
            print("Please enter the speed in km/h format ")
            kmh = input("Enter the speed in Kilometers per Hour (km/h): ")
        km, hr = kmh.split("/")
        real_km = int(km) / int(hr)
        mile = int(real_km) * 0.621371
        return f"The speed in Miles per Hour (mph) is {'%.2f' % mile} miles per hour"
    elif int(opt) == 2:
        mile2 = input("Enter the speed in Miles per Hour (miles/h): ")
        while "/" not in mile2:
            print("Please enter the speed in miles/h format ")
            mile2 = input("Enter the speed in Miles per Hour (mph): ")
        mile3, hr2 = mile2.split("/")
        real_mile = int(mile3) / int(hr2)
        km2 = int(real_mile) * 1.60934
        return f"The speed in Kilometers per Hour (km/h) is {'%.2f' % km2} Kilometers per hour"
    elif int(opt) == 3:
        kmh2 = input("Enter the speed in Kilometers per Hour (km/h): ")
        while "/" not in kmh2:
            print("Please enter the speed in km/h format ")
            kmh2 = input("Enter the speed in Kilometers per Hour (km/h): ")
        km3, hr3 = kmh2.split("/")
        real_km2 = int(km3) / int(hr3)
        meter = (int(real_km2) * 1000) / 3600
        return f"The speed in Meters per Second (m/s) is {'%.2f' % meter} meters per second"
    elif int(opt) == 4:
        ms = input("Enter the speed in Meters per Second (m/s): ")
        while "/" not in ms:
            print("Please enter the speed in m/s format ")
            ms = input("Enter the speed in Meters per Second (m/s): ")
        meter2, sec = ms.split("/")
        real_meter = int(meter2) / int(sec)
        km4 = int(real_meter) * 3.600
        return f"The speed in Kilometers per Hour (km/h) is {'%.2f' % km4} km per hour"
    else:
        return "Invalid input"

if __name__ == "__main__":
    main() 