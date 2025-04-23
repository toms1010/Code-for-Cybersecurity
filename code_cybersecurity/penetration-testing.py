# Basic Port Scanner for Penetration Testing
# Disclaimer: This is for educational purposes only. Use only on systems you own or have permission to test.

import socket
from datetime import datetime

# Function to scan ports
def port_scan(target_ip, start_port, end_port):
    print(f"Starting port scan on target: {target_ip}")
    print(f"Scanning ports {start_port} to {end_port}...\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)  # Set timeout to 1 second

            # Attempt to connect to the port
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: Open")
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            break
        except socket.error:
            print(f"Could not connect to port {port}")

    return open_ports

# Function to validate IP address
def validate_ip(ip):
    try:
        socket.inet_aton(ip)                                                         # Check if the IP address is valid
        return True
    except socket.error:
        return False

# Function to validate numeric input
def validate_number(input_prompt):
    while True:
        user_input = input(input_prompt)
        user_input = input(input_prompt)
        if user_input.isdigit():                                                      # Check if the input is a number
            return int(user_input)
        else:
            print("Invalid input. Must be a number. Please try again.")

# Main program
if __name__ == "__main__":
    # Input target IP and validate it
    while True:
        target_ip = input("Enter the target IP address: ")
        if validate_ip(target_ip):
            break
        else:
            print("Invalid IP address. Please try again.")

    # Input port range and validate it
    start_port = validate_number("Enter the starting port number: ")
    end_port = validate_number("Enter the ending port number: ")

    # Ensure the starting port is less than or equal to the ending port
    while start_port > end_port:
        print("Starting port must be less than or equal to the ending port. Please try again.")
        start_port = validate_number("Enter the starting port number: ")
        end_port = validate_number("Enter the ending port number: ")

    # Start the scan
    start_time = datetime.now()
    open_ports = port_scan(target_ip, start_port, end_port)
    end_time = datetime.now()

    # Print results
    print("\nScan completed!")
    print(f"Open ports: {open_ports}")
    print(f"Time taken: {end_time - start_time}")



    #python penetration-testing.py for the code to run/ to put on the cmd 