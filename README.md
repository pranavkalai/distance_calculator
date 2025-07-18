# Travel Time Automation Tool 
This project is a Python utility designed to calculate distances and durations between a list of origin and destination pairs using the Google Maps Distance Matrix API. It reads location data from an Excel file, processes the API response, and writes the calculated distances and durations back into the same Excel file.

## Features
- Reads origin and destination addresses from a specified Excel file.
- Encodes addresses for use in Google Maps API requests.
- Fetches distance and duration data using the Google Maps Distance Matrix API.
- Extracts diagonal elements (corresponding origin-destination pairs) from the API response (effcient for a large list of address pairs).
- Updates the input Excel file with new 'Distance' and 'Duration' columns.
