def main():
    print_square(3)

# Definiuję funkcję do wklejania kwadratu ale rozbijam to dodatkową funkcję,
# która będzie wklejać rowki
def print_square(size):
    for i in range(size):
        print_row(size)

# Tutaj tworzę funkcję, która wkleja rowki w długości "width"
def print_row(width):
    print("#" * width)

main()
