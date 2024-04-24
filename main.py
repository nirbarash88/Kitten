import requests

def get_and_print_favorites():
    url = "https://api.thecatapi.com/v1/favourites"
    headers = {
        "x-api-key": "live_X8xUf7K48hCw79ZXUnykf3Zw3eBjw5N0tsCy7Ix8IF1nL4VLR4Qm9bmJs9q1bz3F"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        favorites = response.json()
        for favorite in favorites:
            # Extracting 'sub_id' and 'created_at' and handling potential missing keys with default values
            sub_id = favorite.get('sub_id', 'Unknown')
            created_at = favorite.get('created_at', 'Unknown time')
            print(f"hello! Im kitten! My sub_id is {sub_id} and I was created at {created_at}")
    else:
        print(f"Failed to retrieve favorites, status code: {response.status_code}")

# You can call this function to execute the actions:
get_and_print_favorites()