# 1. Open a log file, read its content, find all IP addresses
# 2. Count requests from Ips
# 3. Write data to a csv file

import re
from collections import Counter
import csv

# Opens the file amd reads its contents


def reader(filename):
    with open(filename) as f:
        log1 = f.read()
        # - Prints the log contents to confirm they have been read and opened
        print(log1)

        # Each IP address consists of digits(\d) in a range from 1-3({1,3}) separated by a period '\.'
        # Since there are 4 sections like this in each IP address, the expression is repeated 4 times
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

        # This looks for any expression in the file that matches the 'regexp' pattern defined above
        ips_list = re.findall(regexp, log1)

        return ips_list  # - Returns a list of all IP addresses to confirm our regex expression finds the correct type of data

# Counts each occurence of an IP address request and returns the count


def count(ips_list):
    return Counter(ips_list)

# Writes the IP address and the frequency of each into a csv file


def write_csv(counter):
    with open('outut.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP', 'Frequency']

        writer.writerow(header)

        for item in counter:
            writer.writerow((item, counter[item]))


if __name__ == '__main__':
    write_csv(count(reader('log1')))
