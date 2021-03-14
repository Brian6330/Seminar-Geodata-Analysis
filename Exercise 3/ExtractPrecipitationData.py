import sys

if len(sys.argv) < 2:
    print(
        "Please provide a target precipitation file.\nUsage: python thisScript.py precipitation_data.txt \nExiting...")
    sys.exit()

file_path = str(sys.argv[1])


def analyse_precipitation_data(file_path):
    with open(file_path) as f:
        read_data = f.read()
        print(read_data)


if __name__ == '__main__':
    analyse_precipitation_data(file_path)

print("Finished.")
