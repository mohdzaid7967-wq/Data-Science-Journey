with open("practice.txt" , "w") as file:
    file.write("Hii Everyone\nWe are learning File Input and output\nusing java\n")
    file.write("I like java programming")


with open("practice.txt" , "r") as file:
    data = file.read()

new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt" , "w") as file:
    file.write(new_data)