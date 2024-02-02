
# Case 2


def add_device(network):
    device_name = input("Enter device name: ")
    device_type = input("Enter device type: ")
    ip_address = input("Enter IP address: ")

    device = [device_name, device_type, ip_address]
    network.append(device)
    print(f"{device_name} has been added to the network.\n")
    


def display_devices(network):
    if not network:
        print("No devices in the network.")
    else:
        print("List of Devices:")
        for device in network:
            print(f"Name: {device[0]}, Type: {device[1]}, IP Address: {device[2]}")
        print()


def search_device(network):
    search_name = input("Enter device name to search: ")
    for device in network:
        if device[0].lower() == search_name.lower():
            print(f"Device found - Name: {device[0]}, Type: {device[1]}, IP Address: {device[2]}\n")
            return
    print(f"Device '{search_name}' not found in the network.\n")


def filter_devices_by_type(network):
    filter_type = input("Enter device type to filter: ")
    filtered_devices = [device[0] for device in network if device[1].lower() == filter_type.lower()]

    if not filtered_devices:
        print(f"No {filter_type} devices found in the network.\n")
    else:
        print(f"{filter_type} Devices:")
        for device in filtered_devices:
            print(device)
        print()


def remove_device(network):
    remove_name = input("Enter device name to remove: ")
    for device in network:
        if device[0].lower() == remove_name.lower():
            network.remove(device)
            print(f"{remove_name} has been removed from the network.\n")
            return
    print(f"Device '{remove_name}' not found in the network.\n")


def main():
    network = []

    while True:
        print("Network Management System:")
        print("1. Add Device")
        print("2. Display Devices")
        print("3. Search for a Device")
        print("4. Filter Devices by Type")
        print("5. Remove Device")
        print("6. Exit System")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_device(network)
        elif choice == "2":
            display_devices(network)
        elif choice == "3":
            search_device(network)
        elif choice == "4":
            filter_devices_by_type(network)
        elif choice == "5":
            remove_device(network)
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main()
