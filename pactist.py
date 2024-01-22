student = ("dude", 24, "male")

print(student.count("dude"))
print(student.index("male"))

for x in student:
    print(x)
if "dude" in student:
    print("dude you in the wrong class")