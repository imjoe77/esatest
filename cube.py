import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    num = int(sys.argv[1])
    print("User input given")
else:
    script_name = sys.argv[0]
    num = 50
    print("Default inputs taken")

cube = num * num * num

print("Script Name -", script_name)
print("Cube of number is -", cube)
