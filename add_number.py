num = int(input("Enter a number: ")) #user input
# Generate and display the multiplication table
print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
