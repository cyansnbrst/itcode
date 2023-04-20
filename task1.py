print("Enter the day: ")
day = int(input())

print("Enter the month: ")
month = input()

print("Enter the temperature: ")
temperature = int(input())

print(f"Today is the {day} of {month}. It is {temperature} degrees outside")
if temperature < 0:
    print("Today is cold, it's better to stay home")
