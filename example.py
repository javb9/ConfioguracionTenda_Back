from tenda import TendaManager
import scapy

manager = TendaManager('10.60.11.62:8080', 'SiLcOm18')

# Get QOS
online_devices = manager.get_online_devices_with_stats()
blocked_devices = manager.get_black_list()
print ("obtuvo las configuraciones", (online_devices))
# Set QOS
#manager.block_device('74:15:75:89:f7:c3')
#manager.limit_device('<some_mac_address>', '<download_speed>', '<upload_speed>')

# Get current wifi_settings
wifi = manager.get_wifi_settings()

def escanear(direccion_ip):
    solicitud_arp = scapy.ARP(pdst=direccion_ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    # Fusionamos
    solicitud_arp_broadcast = broadcast/solicitud_arp
    respuesta = scapy.srp(solicitud_arp_broadcast, timeout=1)[0] # Con esta instrucción le decimos que queremos que pregunte a cada solicitud dentro del router a quién le pertenece dicha ip.
    lista_clientes = []
    for elemento in respuesta:
        cliente = {"IP": elemento[1].psrc, "MAC Address": elemento[1].hwsrc}
        lista_clientes.append(cliente)
    return (lista_clientes)

clientesConectados = escanear("192.168.0.1/24")
print("clientes conectados: ", (clientesConectados))

print ("obtuvo las configuraciones", (wifi))
manager.set_wifi_settings("123456")

# Reboot
#manager.reboot()