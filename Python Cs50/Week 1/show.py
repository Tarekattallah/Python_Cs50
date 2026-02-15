SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron ",
    "the Proud family"
]

def main():
    cleaned_shows = [] # create an empty list to store the cleaned show names
    for show in SHOWS: # iterate through each show in the SHOWS list
        cleaned_shows.append(show.strip().title()) # remove whitespace from the show name and convert it to title case, then add it to the cleaned_shows list
    for show in cleaned_shows: # iterate through each cleaned show name in the cleaned_shows list
        print(show) # print the cleaned show name