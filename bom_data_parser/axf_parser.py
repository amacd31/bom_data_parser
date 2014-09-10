import csv

def read_axf(axf_string):
    blocks = {}
    state = 'new_block'

    for line in axf_string.split('\n'):
        if line == '[$]' or line == '':
            pass

        elif line.startswith('['):
            block_key = line.replace('[',"").replace(']',"")
            print block_key

        else:
            if block_key not in blocks:
                blocks[block_key] = []
            blocks[block_key].append(line)

    for k in blocks.keys():
        if k == 'data':
            is_data = False
            data_block = {}
            for row in csv.reader(blocks[k]):
                if is_data:
                    data_block[row[1]] = {}
                    for col_name, col_value in zip(header_row, row):
                        data_block[row[1]][col_name] = col_value

                else:
                    header_row = row
                    is_data = True

        else:
            # probably notice or header ... do something awesome with them
            pass

    return data_block


def read_axf_file(axf_file):
    with open(axf_file, 'r') as f:
        return read_axf(f.read())

if __name__ == "__main__":
    print read_axf_file('../tests/data/IDV60700.axf')
