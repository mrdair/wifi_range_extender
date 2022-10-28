from job_functions import *

# read config file
config = read()

# read nmconnection
nmconnection = nmconnection()

# nmconnection bash
nmconnection_bash(config, nmconnection)

# read interfaces
interfaces = interfaces()

# interfaces bash
interfaces_bash(config, interfaces)
