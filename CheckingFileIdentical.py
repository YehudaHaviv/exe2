import sys

def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines_file1 = file1.readlines()
        lines_file2 = file2.readlines()

    # Compare line by line
    for line_num, (line1, line2) in enumerate(zip(lines_file1, lines_file2), start=1):
        if line1 != line2:
            print(f"Difference found at line {line_num}:")
            print(f"File 1: {line1.strip()}")
            print(f"File 2: {line2.strip()}")
            print()
            return
   
    # If no differences found
    print("Files are identical.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py file1.txt file2.txt")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]

    compare_files(file1_path, file2_path)
