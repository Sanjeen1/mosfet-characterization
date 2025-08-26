def calculate_DIBL():
    # Taking user inputs
    VTH_low = float(input("Enter VTH at VDS_low (in Volts): "))
    VTH_high = float(input("Enter VTH at VDS_high (in Volts): "))
    VDS_low = float(input("Enter VDS_low (in Volts): "))
    VDS_high = float(input("Enter VDS_high (in Volts): "))

    # Applying formula
    DIBL = (VTH_low - VTH_high) / (VDS_high - VDS_low)

    print(f"\nDIBL = {DIBL} V/V")
    print(f"DIBL = {DIBL * 1000:.2f} mV/V")  # Usually expressed in mV/V

# Run function
calculate_DIBL()
