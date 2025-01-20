import argparse
from question1.add import add

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Add two numbers.")
    
    # Add arguments for the two numbers
    parser.add_argument("num1", type=int, help="The first number")
    parser.add_argument("num2", type=int, help="The second number")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Calculate the sum
    result = add(args.num1, args.num2)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
