def read():
    config = open('/home/pi/files/config').readlines()
    return [config[0].strip(), config[1].strip()]


def generate(config):
    interfaces = "source-directory /etc/network/interfaces.d\n" \
                 "auto tplink\n" \
                 "iface tplink inet dhcp\n" \
                 "        wpa-ssid "+config[0]+"\n" \
                 "        wpa-psk  "+config[1]
    open('/home/pi/files/interfaces', 'w').write(interfaces)


def bash():
    import os
    os.system('sudo cp /home/pi/files/interfaces /etc/network/interfaces')
    os.system('sudo reboot')
