"""""Determine the standard deviation of all numbers in the file.

This program will take a CSV data file output the standard deviation of all the numbers in the file printed in the terminal

"""
from mrjob.job import MRJob
import csv
import statistics as st


def csv_readlines(line):
    """Given a sting CSV line, return a list of strings."""
    line = []
    for row in csv.reader(line, delimiter="\t"):
        line.append(row)

class MRfindStdev(MRJob):
    def mapper(self, numbers, line):
        """Extracts value in lines"""
        for numbers in line.split(','):
            # convert the strings to integers.
            numbers = int(numbers)
            #return the KEY/VALUE.
            yield 1, numbers
            #Reduce function applied to all the values that share the same key.
    def reducer(self, occurrences, numbers):
        # calculating the standard deviation for all the numbers. 
        numbers = st.stdev(numbers)
        title="The standard deviation ="
        #output in terminal, the title and the standard devaition rounded to two decimal place.
        yield title, round(numbers,2)
            

if __name__ == '__main__':
    MRfindStdev.run()



   