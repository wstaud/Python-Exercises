import sys
import os
import math

def promptUser():
	print("Ohm's Law Calculator: Python Edition")
	print("\n")

	voltage = input("Enter Voltage(v) if known: (leave blank and press enter if not)")
	print("\n")

	# Amps
	current = input("Enter Current(i) in amps if known: (leave blank and press enter if not)")
	print("\n")

	# Ohms
	resistance = input("Enter Resistance(R) in ohms if known: (leave blank and press enter if not)")
	print("\n")

	power = input("Enter Power(P) in watts if known: (leave blank and press enter if not)")

	if voltage:
		voltage = float(voltage)
		if current:
			current = float(current)
			return vC(voltage, current)
		elif resistance:
			resistance = float(resistance)
			return vR(voltage, resistance)
		elif power:
			power = float(power)
			return vP(voltage, power)
		else:
			print("ERROR: Missing a value")
	elif current:
		current = float(current)
		if resistance:
			resistance = float(resistance)
			return cR(current, resistance)
		elif power:
			power = float(power)
			return cP(current, power)
		else:
			print("ERROR: Missing a value")
	elif (resistance) and (power):
		resistance = float(resistance)
		power = float(power)
		return rP(resistance, power)
	else:
		print("ERROR: Ensure you left empty values blank and you inputted at least two values.")

# Calculation based functions

# Calculate Power and Ohms
def vC(voltage, current):
	p = voltage * current
	r = voltage / current

	print("Power is %.2f watts and Resistance is %.2f ohms." % (p, r))

# Calculate Amps and Power
def vR(voltage, resistance):
	i = voltage / resistance
	p = voltage**2 / resistance

	print("Current is %.2f amps and Power is %.2f watts." % (i, p))

# Calculate Amps and Ohms
def vP(voltage, power):
	i = power / voltage
	r = voltage**2 / power

	print("Current is %.2f amps and Resistance is %.2f ohms." % (i, r))

# Calculate Volts and Power
def cR(current, resistance):
	e = current * resistance
	p = current**2 * resistance

	print("Voltage is %.2f volts and Power is %.2f watts." % (e, p))

# Calculate Volts and Ohms
def cP(current, power):
	e = power / current
	r = power / current**2

	print("Voltage is %.2f volts and Resistance is %.2f ohms."% (e, r))

# Calculate Amps and Volts
def rP(resistance, power):
	i =  math.sqrt(power/resistance)
	e = math.sqrt(power*resistance)

	print("Current is %.2f amps and Voltage is %.2f voltage" % (i, e))

promptUser()


