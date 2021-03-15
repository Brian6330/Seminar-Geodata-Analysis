import sys
import statistics

if len(sys.argv) < 2:
    print(
        "Please provide a target precipitation file.\nUsage: python thisScript.py precipitation_data.txt \nExiting...")
    sys.exit()

file_path = str(sys.argv[1])


def analyse_precipitation_data(precipitation_file_path):
    header_line = 1
    stn = []
    time = []
    precip = []

    with open(precipitation_file_path) as f:
        for line_number, line in enumerate(f, 1):
            # Skip header
            if line_number <= header_line:
                continue
            # Split lines into its columns and assign the columns to array lists
            linesplit = line.strip().split()
            stn.append(linesplit[0])
            time.append(int(linesplit[1]))
            precip.append(float(linesplit[2]))

    # Use statistics to calculate mean, and built-in min & max functions
    mean_precip = statistics.mean(precip)
    min_precip = min(precip)
    max_precip = max(precip)

    # Print the calculated values
    print("The average precipitation is {}, while the minimum is {} and the maximum is {}"
          .format(mean_precip, min_precip, max_precip))


if __name__ == '__main__':
    analyse_precipitation_data(file_path)

print("Finished.")
