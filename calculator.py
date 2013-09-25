import arithmetic

def main():    
    while True:
        number_input = raw_input("> ")
        tokens = number_input.split(" ")
        if tokens[0] == "q":
            quit()
        if tokens[0] == "+":
            print arithmetic.add(int(tokens[1]), int(tokens[2]))
        if tokens[0] == "-":
            print arithmetic.subtract(int(tokens[1]), int(tokens[2]))
        if tokens[0] == "*":
            print arithmetic.multiply(int(tokens[1]), int(tokens[2]))
        if tokens[0] == "/":
            print arithmetic.divide(int(tokens[1]), int(tokens[2]))
        if tokens[0] == "square":
            print arithmetic.square(int(tokens[1]))
        if tokens[0] == "cube":
            print arithmetic.cube(int(tokens[1]))
        if tokens[0] == "pow":
            print arithmetic.power(int(tokens[1]), int(tokens[2]))
        if tokens[0] == "mod":
            print arithmetic.mod(int(tokens[1]), int(tokens[2]))
main()