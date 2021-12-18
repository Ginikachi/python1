import time_series

def smallest_value_skip(reader):
    """ (file open for reading) -> number or NoneType
    Read and process reader, which must start with a time_series header.
    Return the smallest value after the header. Skip missing values which
    are indicated with a hyphen.
    """

    line = time_series.skip_header(reader).strip()
    # Only execute this code, if there is data following the header.
    if line != '':
        smallest = int(line)

        for line in reader:
            line = line.strip()
            if line != '-':
                value = int(line)
                smallest = min(smallest, value)

        return smallest
    
        
if __name__ == '__main__':
    with open('hebron_modified.txt', 'r') as input_file:
        print(smallest_value_skip(input_file))

## Notice that the update to smallest is nested inside the check for hyphens;
## i.e.   if line != '-':
##            value = int(line)
##            smallest = min(smallest, value)     

