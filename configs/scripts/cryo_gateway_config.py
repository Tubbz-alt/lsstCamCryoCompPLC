

from umodbus import conf
from umodbus.client import tcp
import socket
import time


a = [0]*42

class PlutoGateway():

    def __init__(self, ip , port):
        # Enable values to be signed (default is False).
        conf.SIGNED_VALUES = False

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))





    def gateway_config_write_read(self,add, value):
        config_id = 4

        message = tcp.write_multiple_registers(slave_id=config_id, starting_address=add, values=[value])
        response = tcp.send_message(message, self.sock)

        time.sleep(0.1)

        message = tcp.read_holding_registers(config_id, add, 1)
        response = tcp.send_message(message, self.sock)

        print("..")

        global a
        a[add]=value

        if response[0] != value:
            raise ValueError("Value not writen!")

    def close(self):
        self.sock.close()




#plutoGateway = PlutoGateway('192.168.1.170', 502)
#plutoGateway = PlutoGateway('192.168.1.172', 502)
plutoGateway = PlutoGateway('192.168.1.174', 502)
#plutoGateway = PlutoGateway('192.168.1.176', 502)
#plutoGateway = PlutoGateway('192.168.1.178', 502)
#plutoGateway = PlutoGateway('192.168.1.180', 502)
#plutoGateway = PlutoGateway('192.168.1.182', 502)
#plutoGateway = PlutoGateway('192.168.1.184', 502)
#plutoGateway = PlutoGateway('192.168.1.186', 502)
#plutoGateway = PlutoGateway('192.168.1.188', 502)
#plutoGateway = PlutoGateway('192.168.1.190', 502)
#plutoGateway = PlutoGateway('192.168.1.192', 502)


# Reset all registers to 0
for add in range(0,41+1):
    plutoGateway.gateway_config_write_read(add, 0x00)

# Activate Data to Pluto Area 0,1
plutoGateway.gateway_config_write_read(1,0b001)

# Data to Pluto Timeout = 0
plutoGateway.gateway_config_write_read(2,0)

# Additional Data Areas for PLC 0
plutoGateway.gateway_config_write_read(5,0x01)
plutoGateway.gateway_config_write_read(6,0x02)
plutoGateway.gateway_config_write_read(7,0x03)
plutoGateway.gateway_config_write_read(8,0x04)
plutoGateway.gateway_config_write_read(9,0x05)
plutoGateway.gateway_config_write_read(10,0x06)
plutoGateway.gateway_config_write_read(11,0x07)
plutoGateway.gateway_config_write_read(12,0x08)
plutoGateway.gateway_config_write_read(13,0x09)
plutoGateway.gateway_config_write_read(14,0x0A)
plutoGateway.gateway_config_write_read(15,0x0B)
plutoGateway.gateway_config_write_read(16,0x0C)
plutoGateway.gateway_config_write_read(17,0x0D)
plutoGateway.gateway_config_write_read(18,0x0E)
plutoGateway.gateway_config_write_read(19,0x0F)



# Data to Pluto Cycle time = 100 ms
plutoGateway.gateway_config_write_read(37,100)

# Gateway Node number = 0
plutoGateway.gateway_config_write_read(41,0x001)


print ("Done")

print(a)


plutoGateway.close()


