import requests
from bs4 import BeautifulSoup

url = "https://www.shadowfox.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

jls_extract_var = soup
company_name = jls_extract_var.find('h1', class_='company-name').text.strip()
tagline = soup.find('p', class_='tagline').text.strip()
services = soup.find_all('li', class_='service')
team_members = soup.find_all('div', class_='team-member')

print("Company Name:", company_name)
print("Tagline:", tagline)
print("Services:")
for service in services:
    print(service.text.strip())
print("Team Members:")
for member in team_members:
    print(member.find('h2', class_='name').text.strip())