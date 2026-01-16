# cube.py
import sys

def cube(num):
    return num * num * num

if __name__ == "__main__":
    if len(sys.argv) == 2:
        script_name = sys.argv[0]
        num = int(sys.argv[1])
        print("User input given")
    else:
        script_name = sys.argv[0]
        num = 50
        print("Default inputs taken")

    result = cube(num)

    print("Script Name -", script_name)
    print("Cube of number is -", result)
