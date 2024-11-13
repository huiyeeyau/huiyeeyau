import json
import requests

def get_singer():
    while True:
        singer = input("Enter the singer's name: ")
        if not singer.isalpha():
            print("Please enter a valid singer name with alphabetic characters.")
        elif len(singer) <= 0:
            print("Please enter a singer name.")
        else:
            return singer

def get_limit():
    while True:
        try:
            limit = int(input("Enter the limit for the number of songs to retrieve: "))
            if limit <= 0:
                print("Limit must be a positive integer. Please try again.")
                continue
            else:
                return limit
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    singer = get_singer()
    limit = get_limit()

    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={limit}&term={singer}")
    data = response.json()

    for result in data["results"]:
        print(result["trackName"])

if __name__ == "__main__":
    main()
