import time_series
def process_file(reader):
    """ (file open for reading) -> NoneType

    Read and print the data from reader, which must start with a single
    description line, then a sequence of lines beginning with '#', then a
    sequence of data.
    """

    line = time_series.skip_header(reader).strip()
    print(line)
    line = reader.read()
    print(line)

if __name__ == '__main__':
    with open('Lynx.txt', 'r') as Lynx:
        process_file(Lynx)
    
