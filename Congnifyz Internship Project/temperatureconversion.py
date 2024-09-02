def convert_temperature():
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()

    if unit == 'C':
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {converted_temp:.2f}°F")
    elif unit == 'F':
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

while True:
    convert_temperature()
    continue_prompt = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        print("Exiting the program.")
        break
