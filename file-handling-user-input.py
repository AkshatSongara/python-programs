text = input("Enter a text: ")

with open("student.txt", "w") as file:

    file.write(text)

with open("student.txt", "r") as file:

    data = file.read()

print("File Data:", data)