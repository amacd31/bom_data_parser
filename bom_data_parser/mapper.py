mappings = {
            'airtemp_min': ['MIN TEMP', 'Minimum temperature (Degree C)'],
            'airtemp_max': ['MAX TEMP', 'Maximum temperature (Degree C)'],
        }

def convert_key(input_key):
    for key in mappings.keys():
        if input_key in mappings[key]:
            return key
    else:
        return input_key
