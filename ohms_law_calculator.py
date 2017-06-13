"""Ohms Law Calc"""
import math

def prompt_user():
    """Prompts user for input"""
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
            return volt_current(voltage, current)
        elif resistance:
            resistance = float(resistance)
            return volt_resistance(voltage, resistance)
        elif power:
            power = float(power)
            return volt_power(voltage, power)
        else:
            print("ERROR: Missing a value")
    elif current:
        current = float(current)
        if resistance:
            resistance = float(resistance)
            return current_resistance(current, resistance)
        elif power:
            power = float(power)
            return current_power(current, power)
        else:
            print("ERROR: Missing a value")
    elif (resistance) and (power):
        resistance = float(resistance)
        power = float(power)
        return resistance_power(resistance, power)
    else:
        print("ERROR: Ensure you left empty values blank and you inputted at least two values.")

# Calculation based functions

def volt_current(voltage, current):
    """Calculate Power and Ohms"""
    power = voltage * current
    resistance = voltage / current

    print("Power is {:.2f} watts and Resistance is {:.2f} ohms.".format(power, resistance))

def volt_resistance(voltage, resistance):
    """# Calculate Amps and Power"""
    current = voltage / resistance
    power = voltage**2 / resistance

    print("Current is {:.2f} amps and Power is {:.2f} watts.".format(current, power))

def volt_power(voltage, power):
    """Calculate Amps and Ohms"""
    current = power / voltage
    resistance = voltage**2 / power

    print("Current is {:.2f} amps and Resistance is {:.2f} ohms.".format(current, resistance))

def current_resistance(current, resistance):
    """Calculate Volts and Power"""
    voltage = current * resistance
    power = current**2 * resistance

    print("Voltage is {:.2f} volts and Power is {:.2f} watts.".format(voltage, power))

def current_power(current, power):
    """Calculate Volts and Ohms"""
    voltage = power / current
    resistance = power / current**2

    print("Voltage is {:.2f} volts and Resistance is {:.2f} ohms.".format(voltage, resistance))

def resistance_power(resistance, power):
    """Calculate Amps and Volts"""
    current = math.sqrt(power/resistance)
    voltage = math.sqrt(power*resistance)

    print("Current is {:.2f} amps and Voltage is {:.2f} voltage".format(current, voltage))

# Call Menu
prompt_user()
