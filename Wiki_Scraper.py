import requests
from bs4 import BeautifulSoup

def get_wiki_data(name):
    # Search for the page title first to handle redirects/variations
    search_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": name,
        "format": "json"
    }
    headers = {"User-Agent": "MyGenerativeAILab/1.0 (aditya@example.com)"}
    res = requests.get(search_url, params=params, headers=headers)
    try:
        search_res = res.json()
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        print("Response text:", res.text[:500])
        return
    
    if not search_res['query']['search']:
        print(f"No Wikipedia page found for '{name}'.")
        return

    title = search_res['query']['search'][0]['title']
    page_url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
    print(f"\nFetching data from: {page_url}")

    # Get Summary via API
    summary_params = {
        "action": "query",
        "prop": "extracts",
        "exsentences": 2,
        "titles": title,
        "explaintext": 1,
        "format": "json"
    }
    summary_res = requests.get(search_url, params=summary_params, headers=headers).json()
    pages = summary_res['query']['pages']
    summary_text = pages[list(pages.keys())[0]]['extract']

    # Get Infobox via scraping
    soup = BeautifulSoup(requests.get(page_url, headers=headers).text, 'html.parser')
    infobox = soup.select_one('.infobox')
    
    details = {}
    if infobox:
        for tr in infobox.select('tr'):
            th = tr.find('th')
            td = tr.find('td')
            if th and td:
                key = th.get_text().strip().lower()
                val = td.get_text().strip()
                if any(x in key for x in ['founded', 'established', 'headquarters', 'location']):
                    details[key.capitalize()] = val

    print("\n--- Details ---")
    if details:
        for k, v in details.items():
            print(f"{k}: {v}")
    else:
        print("No foundation or HQ info found.")

    print("\n--- Summary ---")
    print(summary_text)

if __name__ == "__main__":
    name = input("Enter institution name (e.g., 'Google', 'Harvard University'): ")
    try:
        get_wiki_data(name)
    except Exception as e:
        print(f"Error: {e}")
