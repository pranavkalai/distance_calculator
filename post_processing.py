import pandas as pd

def get_diagonal(matrix):
    length = len(matrix['destination_addresses'])
    distances = [matrix["rows"][index]["elements"][index]["distance"]["text"] for index in range(0, length)]
    durations = [matrix["rows"][index]["elements"][index]["duration"]["text"] for index in range(0, length)]
    return (distances, durations)

def write(file_name, tuple):
    df = pd.read_excel(file_name)
    df['Distance'] = tuple[0]
    df['Duration'] = tuple[1]
    df.to_excel(file_name, index = False)