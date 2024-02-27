''''

Given the temperature at which water begins to boil, 
determine atmospheric pressure.

'''

# Ask user for temperature
temperature_b = int(input("What is the temperature at which water begins to boil?: "))

# Methematical solutions to find atmoshpheric pressure
atmospheric_p = 5 * temperature_b - 400

# Result
print("The atmopsheric pressure is " + str(atmospheric_p) + " when the temperetaure at which water boils is " + str(temperature_b))

