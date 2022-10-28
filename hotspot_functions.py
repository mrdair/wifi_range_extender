def read():
    config = open('/home/pi/files/config').readlines()
    return [config[2].strip(), config[3].strip()]


def generate(config):
    nmconnection = "[connection]\n" \
      "id=intel-extender\n" \
      "uuid=7b13be08-5bca-42fe-99db-44244c92b7de\n" \
      "type=wifi\n" \
      "interface-name=intel\n" \
      "permissions=\n" \
      "\n" \
      "[wifi]\n" \
      "band=bg\n" \
      "mac-address-blacklist=\n" \
      "mode=ap\n" \
      "ssid="+config[0]+"\n" \
      "\n" \
      "[wifi-security]\n" \
      "key-mgmt=wpa-psk\n" \
      "psk="+config[1]+"\n" \
      "\n" \
      "[ipv4]\n" \
      "dns-search=\n" \
      "method=shared\n" \
      "\n" \
      "[ipv6]\n" \
      "addr-gen-mode=stable-privacy\n" \
      "dns-search=\n" \
      "method=auto\n"
    open('/home/pi/files/intel-extender.nmconnection', 'w').write(nmconnection)


def bash():
  import os
  os.system('sudo cp /home/pi/files/intel-extender.nmconnection /etc/NetworkManager/system-connections/intel-extender.nmconnection')
  os.system('sudo reboot')
