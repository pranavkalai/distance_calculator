import pandas as pd

def load_locations(file_name):
    df = pd.read_excel(file_name)
    orgins = [row['Orgin'] for index, row in df.iterrows()]
    destinations = [row['Destination'] for index, row in df.iterrows()]
    return [orgins, destinations]

def encode(string):
    # space = '%20'
    # comma = '%2C'
    
    string = '%20'.join(string.split())
    string = '%2C'.join(string.split(','))
    return string

def encode_locations(list):
    for i in range(0, len(list[0])):
        list[0][i] = encode(list[0][i])
    for i in range(0, len(list[1])):
        list[1][i] = encode(list[1][i])

def get_url_parms(file_name):
    list = load_locations(file_name)
    encode_locations(list)
    url_orgins = '|'.join(list[0])
    url_destinations = '|'.join(list[1])
    return (url_orgins, url_destinations)

# file = 'test.xlsx'

# print(get_url_parms(file))
            