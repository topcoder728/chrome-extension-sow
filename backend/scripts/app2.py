from bs4 import BeautifulSoup
import re
import json

def func1(html_code):
    extracted_data = []
    soup = BeautifulSoup(html_code, 'html.parser')
    intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
    name_loc = intro.find("h1")
    name = name_loc.get_text().strip()
    works_at_loc = intro.find("div", {'class': 'text-body-medium'})
    works_at = works_at_loc.get_text().strip()
    location_loc = soup.find("span", {'class': 'text-body-small inline t-black--light break-words'}).text
    ul_element = soup.find('ul', class_='pvs-list')
    div_element = soup.find('div', class_='display-flex align-items-center mr1 hoverable-link-text t-bold')
    company_name_element = div_element.find('span', {'aria-hidden': 'true'}).text
    div_ele1 = div_element.find_next('div', class_='display-flex align-items-center mr1 hoverable-link-text t-bold')
    position = div_ele1.find('span', {'aria-hidden': 'true'}).text
    time = soup.find('span', class_="t-14 t-normal")
    time = soup.find('span', class_="t-14 t-normal")
    if time:
        time = time.contents[0].strip()
    else:
        time = ''
    experience_text = f"Company: {works_at}\nPosition: {position}\nTime: {time}\n"
    formatted_data = {
        "Name": name,
        "Current Job": works_at,
        "Location": location_loc.strip(),
        "Experience": {
            "Company": works_at,
            "Position": position,
            "Time": time
        },
        "About":""
    }
    return formatted_data
    # Append the data to the JSON file

