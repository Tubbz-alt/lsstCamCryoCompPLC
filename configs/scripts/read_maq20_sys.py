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
print(maq20)
