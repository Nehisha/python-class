# 1.

class Converter:

    def celcius_to_fahrenhite(self):
        temperature = float(input("Enter the temperature in celcius: "))
        celcius = (temperature - 32) * 5 / 9
        print(celcius)

    def faherhite_to_celcius(self):
        temperature = float(input("Enter the Temperature in Fahrenheit: "))
        fahrenhite = (temperature * 9 / 5) + 32
        print(fahrenhite)

    # def convert(self):
    #     user_choice = input("Convert to Celcius of Fahrenhite? (C/F): ").upper
    #     if user_choice == "C":
    #         self.faherhite_to_celcius()
    #     elif user_choice == "F":
    #         self.celcius_to_fahrenhite()
    #     else:
    #         print("invalid choice")


temp = Converter()
temp.celcius_to_fahrenhite()
temp.faherhite_to_celcius()
