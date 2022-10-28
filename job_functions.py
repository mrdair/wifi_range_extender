def read():
    config = open('/home/pi/files/config').readlines()
    return [config[0].strip(), config[1].strip(), config[2].strip(), config[3].strip()]


def nmconnection():
    config = open('/etc/NetworkManager/system-connections/intel-extender.nmconnection').readlines()
    ssid = config[11].split('=')[1].strip()
    password = config[15].split('=')[1].strip()
    return [ssid, password]


def interfaces():
    config = open('/etc/network/interfaces').readlines()
    ssid = config[3].split()[1]
    password = config[4].split()[1]
    return [ssid, password]


def nmconnection_bash(config, nmconnection):
    if config[2] != nmconnection[0] or config[3] != nmconnection[1]:
        import os
        os.system('sudo python /home/pi/hotspot_main.py')


def interfaces_bash(config, interfaces):
    if config[0] != interfaces[0] or config[1] != interfaces[1]:
        import os
        os.system('sudo python /home/pi/wifi_main.py')
