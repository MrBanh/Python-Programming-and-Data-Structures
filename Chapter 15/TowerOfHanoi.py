def main():
    n = int(input("Enter number of disks: "))

    # Find solution recursively
    print("The moves are:")
    move_disk(n, 'A', 'B', 'C')


def move_disk(n, from_tower, to_tower, aux_tower):
    if n == 1:      # Only 1 disk, stopping condition
        print("Move disk", n, "from", from_tower, "to", to_tower)
    else:
        # Move (n - 1) disks from_tower to aux_tower
        move_disk(n - 1, from_tower, aux_tower, to_tower)
        # Move disk n from_tower to to_tower
        print("Move disk", n, "from", from_tower, "to", to_tower)
        # Move disk n - 1 aux_tower to to_tower
        move_disk(n - 1, aux_tower, to_tower, from_tower)


if __name__ == "__main__":
    main()
