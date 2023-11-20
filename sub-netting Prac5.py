def calculate_subnet_masks(ip_address, num_subnets):
    # Split the IP address into octets
    octets = list(map(int, ip_address.split('.')))

    # Calculate the number of bits needed for the subnets
    num_bits = num_subnets.bit_length()

    # Calculate the subnet mask for the given number of subnets
    subnet_mask = [255, 255, 255, 255]
    for i in range(4):
        if num_bits >= 8:
            subnet_mask[i] = 255
            num_bits -= 8
        else:
            subnet_mask[i] = 256 - 2**(8 - num_bits)
            num_bits = 0

    # Calculate the size of each subnet
    subnet_size = 2**(8 - num_bits)

    return subnet_mask, subnet_size

def main():
    # Get user input
    ip_address = input("Enter the IP address: ")
    num_subnets = int(input("Enter the number of subnets: "))

    # Calculate subnet masks
    subnet_mask, subnet_size = calculate_subnet_masks(ip_address, num_subnets)

    # Display results
    print("\nSubnet Masks:")
    print("Subnet #\tSubnet Mask")
    for i in range(num_subnets):
        subnet_address = ".".join(map(str, subnet_mask))
        print(f"{i+1}\t\t{subnet_address}")
        # Calculate the next subnet mask
        subnet_mask[-1] += subnet_size
        for j in range(3, 0, -1):
            if subnet_mask[j] > 255:
                subnet_mask[j] -= 256
                subnet_mask[j-1] += 1

if __name__ == "__main__":
    main()
