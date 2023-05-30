import socket

def ping_with_port(ip_address, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Set a timeout value (in seconds)

        # Attempt to connect to the IP address and port
        result = sock.connect_ex((ip_address, port))

        # Check if the connection was successful
        if result == 0:
            print(f"Port {port} is open on {ip_address}")
        else:
            print(f"Port {port} is closed on {ip_address}")

        # Close the socket
        sock.close()

    except socket.error as e:
        print("An error occurred:", e)

# Example usage
ip_address = "192.168.0.1"
port = 80
ping_with_port(ip_address, port)
