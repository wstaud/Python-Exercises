import sys
import os

def promptUser():
	print("Ohm's Law Calculator: Python Edition")
	print("\n")

	print("Enter Voltage(v) if known: (leave blank and press enter if not)")
	voltage = sys.stdnin.readLine()
	print("\n")

	print("Enter Current(i) in amps if known: (leave blank and press enter if not)")
	current = sys.stdnin.readLine()
	print("\n")

	print("Enter Resistance(R) in ohms if known: (leave blank and press enter if not)")
	resistance = sys.stdnin.readLine()
	print("\n")

	print("Enter Power(P) in watts if known: (leave blank and press enter if not)")
	power = sys.stdin.readLine()

	if voltage:
		if current:
			return vC(voltage, current)
		elif resistance:
			return vR(voltage, current)
		elif power:
			return vP(voltage, power)
		else:
			return "Error"
	else: return None

def vC(voltage, current):


def vR(voltage, resistance):


def vP(voltage, power):




