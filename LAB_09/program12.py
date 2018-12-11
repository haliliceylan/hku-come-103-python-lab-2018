def kinetic_energy(m, v):
    return 0.5 * (m * v**2)


def main():
    mass = int(input("Enter the mass of the object in kilogram: "))
    velocity = int(input("Enter the object velocity in meter per second: "))
    ke = kinetic_energy(mass, velocity)
    print("Kinetic Energy is:", format(ke, ".2f"), "joules")


if __name__ == "__main__":
    main()
    pass
