f = open("D:\Data Science Journey\Advance Python Concept\File input-output\greek.txt", "r")


print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)