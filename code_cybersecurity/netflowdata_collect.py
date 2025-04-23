

import random
from collections import defaultdict

# Simulate a network flow
class NetworkFlow:
    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol, bytes_sent):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
        self.protocol = protocol
        self.bytes_sent = bytes_sent

    def __repr__(self):
        return (f"Flow: {self.src_ip}:{self.src_port} -> {self.dst_ip}:{self.dst_port} "
                f"({self.protocol}), Bytes Sent: {self.bytes_sent}")

# Generate random network flows
def generate_flows(num_flows):
    flows = []
    protocols = ["TCP", "UDP", "ICMP"]
    for _ in range(num_flows):
        src_ip = f"192.168.1.{random.randint(1, 254)}"
        dst_ip = f"10.0.0.{random.randint(1, 254)}"
        src_port = random.randint(1024, 65535)
        dst_port = random.randint(1, 1023)
        protocol = random.choice(protocols)
        bytes_sent = random.randint(100, 10000)
        flows.append(NetworkFlow(src_ip, dst_ip, src_port, dst_port, protocol, bytes_sent))
    return flows

# Analyze NetFlow data
def analyze_flows(flows):
    # Group flows by destination IP
    dst_ip_traffic = defaultdict(int)
    for flow in flows:
        dst_ip_traffic[flow.dst_ip] += flow.bytes_sent

    # Print traffic summary
    print("Traffic Summary by Destination IP:")
    for dst_ip, traffic in dst_ip_traffic.items():
        print(f"{dst_ip}: {traffic} bytes")

    # Find the top talker (source IP with the most bytes sent)

    
    top_talker = max(flows, key=lambda flow: flow.bytes_sent)
    print(f"\nTop Talker: {top_talker.src_ip} sent {top_talker.bytes_sent} bytes to {top_talker.dst_ip}")








if __name__ == "__main__":
    print("NetFlow Data Simulation\n")

    # Generate random network flows
    num_flows = 10
    flows = generate_flows(num_flows)

    # Print generated flows
    print("Generated Network Flows:")
    for flow in flows:
        print(flow)

   
    analyze_flows(flows)