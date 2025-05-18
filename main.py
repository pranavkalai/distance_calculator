from dotenv import load_dotenv
from pre_processing import get_url_parms
from post_processing import get_diagonal, write
import requests
import os

### Pre-Processing ###
def url(destinations, orgins, key):
    return 'https://maps.googleapis.com/maps/api/distancematrix/json?destinations=' + destinations + '&origins=' + orgins + '&key=' + key

file = input('Enter File Name: ')
load_dotenv()
api_key = os.getenv('GOOGLE_MAPS_API_KEY')

locations = get_url_parms(file)

### API ###
response = requests.get(url(locations[1], locations[0], api_key))

### Post-Processing ###
data = get_diagonal(response.json())
write(file, data)

