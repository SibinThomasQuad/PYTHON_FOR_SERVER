from scapy.all import traceroute

def trace_ip_routes(domain):
    # Perform traceroute on the domain
    packets = traceroute(domain)

    # Print the IP routes
    for packet in packets:
        if packet.haslayer('IP'):
            ttl = packet.getlayer('IP').ttl
            src_ip = packet.getlayer('IP').src
            dst_ip = packet.getlayer('IP').dst
            print(f"TTL: {ttl}, Source IP: {src_ip}, Destination IP: {dst_ip}")

# Example usage
domain = "example.com"
trace_ip_routes(domain)
