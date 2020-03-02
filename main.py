import scapy.layers.l2

def main():
    interface_to_scan = None
    list_of_network = []
    for network, netmask, _, interface, address, _ in scapy.config.conf.route.routes:
        if interface_to_scan and interface_to_scan != interface:
            continue
        if network == 0 or interface == 'lo' or address == '127.0.0.1' or address == '0.0.0.0':
            continue
        if netmask <= 0 or netmask == 0xFFFFFFFF:
            continue
        if interface != interface_to_scan and interface.startswith('docker') or interface.startswith('br-'):
            continue
        list_of_network.append(interface)
    print(*list_of_network)

if __name__ == "__main__":
    main()