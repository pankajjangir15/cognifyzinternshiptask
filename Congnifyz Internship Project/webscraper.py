import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('h2')  # Modify this to match the HTML tag you want to scrape
        for title in titles:
            print(title.get_text())
    else:
        print("Failed to retrieve the webpage.")

while True:
    url = input("Enter the URL of the website to scrape: ")
    scrape_titles(url)
    continue_prompt = input("Do you want to scrape another website? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        print("Exiting the program.")
        break
