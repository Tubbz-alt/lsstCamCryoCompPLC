from maq20 import MAQ20



ip = "192.168.1.171"
#ip = "192.168.1.173"
#ip = "192.168.1.175"
#ip = "192.168.1.177"
#ip = "192.168.1.179"
#ip = "192.168.1.181"
#ip = "192.168.1.183"
#ip = "192.168.1.185"
#ip = "192.168.1.187"
#ip = "192.168.1.189"
#ip = "192.168.1.181"
#ip = "192.168.1.193"
#ip = "192.168.1.195"


ip = "192.168.128.100"

maq20 = MAQ20(ip_address=ip, port=502)

for module in maq20:
    # Configure range both TTC-00 and TTC-01
    if module.get_name().find("TTC") > -1:
        module.write_registers(100, [1] * 8)  # Temperature Range -100°C to +220°C
        module.write_register(119, 1)  # Save to EPPROM
        print("Configured", module.get_name(),module.get_serial_number())

    # Configure module-00
    if module.get_name().find("DIOL") > -1:

        if 1:

            #
            # Timer 0 (DO0 and DO2) - PWM output
            #

            module.write_register(1100, 6) # Timer 1 as PMW Generator
            module.write_register(1103, 2) # Microseconds time base
            module.write_register(1104, 1) # Disable output 2

            # Configure DO0 - PWM output
            module.write_registers(1108, [1, 9000]) # Low level PWM (fan speed control)
            module.write_register(1101, 1) # Arm Timer (must be the last thing done)
            module.write_register(1190, 0) # Save to EPPROM



            # Configure DO1 - Coolant Valve
            module.write_register(111, 1)  # Default

            # Configure DO2 - Normal Valve
            module.write_register(112, 1)  # Default

            # Configure D03 - Evac Valve
            module.write_register(113, 1)  # Default

            # Configure D04 - Surge Tank Heater
            module.write_register(114, 1)  # Default


            #
            # Timer 1 (DI2) - Freq Read
            #
            module.write_register(1200, 1)  # Timer 1 as Pulse/Freq
            # Configure DI2 - Fan 2 Speed
            module.write_register(1201, 1)  # Arm Timer (must be the last thing done)
            #module.write_register(1290, 0)  # Save to EPPROM                               ## ERROR????




            module.write_register(190, 0)  # Save to EPPROM

            print("Configured", module.get_name(),module.get_serial_number())





            # Write 1108 and 1109 to control PWM
            # Write 1001 to control Coolant Valve
            # Write 1002 to control Normal Valve 
            # Write 1003 to control Evac Valve
            # Write 1004 to control Surge Tank Heater

            # Read 1206 and 1207 to get the frequency









