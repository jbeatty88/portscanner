import sys
import socket
from datetime import datetime

# USAGE: python3 scanner.py <ip>

# Define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
else:
    print("USAGE: python3 scanner.py <ip>")

# Add a banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)


try:  # Try to walk through all of these ports and search for an open port to connect to
    for port in range(1, 65535):  # TODO: Thread
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 TCP
        socket.setdefaulttimeout(1)  # Default timeout of 1 second
        result = s.connect_ex((target, port))  # Attempt to connect with remote host or error
        if result == 0:  # If the port has been opened
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting program.")
    sys.exit()  # Clean up resources and exit
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Failure to connect to server.")
    sys.exit()

