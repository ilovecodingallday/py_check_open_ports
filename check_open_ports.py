import socket

target_host = input("Enter the target host: ")
min_port = int(input("Enter the minimum port number: "))
max_port = int(input("Enter the maximum port number: "))

# Loop over the specified range of port numbers
for port in range(min_port, max_port + 1):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(0.5)  # Set a timeout for the connection

    # Attempt to connect to the target host and port
    try:
        # Connect to the target host and port
        result = client_socket.connect_ex((target_host, port))

        # Check if the connection was successful
        if result == 0:
            print("Port {}: Open".format(port))
    except Exception as e:
        print("Error: ", e)

    # Close the socket connection
    client_socket.close()
