import socket

# Define the target IP address and port range
target = '127.0.0.1'
port_range = range(1, 100)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Scan the target ports
for port in port_range:
    try:
        # Attempt to connect to the target port
        client_socket.connect((target, port))
        
        # Print a message if the connection was successful
        print(f'Port {port} is open')
        
        # Close the connection
        client_socket.close()
    except:
        # Print a message if the connection failed
        print(f'Port {port} is closed')
