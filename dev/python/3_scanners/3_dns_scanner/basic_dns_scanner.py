import whois
import requests
from bs4 import BeautifulSoup

def get_whois_data(domain_name):
    whois_info = whois.whois(domain_name)
    return whois_info

def get_dnsdumpster_data(domain_name):
    url = f'https://dnsdumpster.com/'
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_middleware_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

    headers = {
        'Referer': 'https://dnsdumpster.com/',
    }

    data = {
        'csrfmiddlewaretoken': csrf_middleware_token,
        'targetip': domain_name,
    }

    response = session.post(url, headers=headers, data=data)
    return response.text

def get_mxtoolbox_data(domain_name):
    url = f'https://mxtoolbox.com/Public/Tools/ToolDetails.aspx'
    params = {'tool=1000': domain_name}
    response = requests.get(url, params=params)
    return response.text

# WHOXY API Key (Sign up to get your own API key)
whoxy_api_key = 'YOUR_WHOXY_API_KEY'

def get_whoxy_data(domain_name):
    url = f'https://api.whoxy.com/?key={whoxy_api_key}&whois=1&identifier={domain_name}'
    response = requests.get(url)
    return response.json()

def main():
    domain_name = input("Enter the domain name: ")

    # WHOIS data
    whois_data = get_whois_data(domain_name)
    print("\nWHOIS Data:")
    print(whois_data)

    # DNSDumpster data
    dnsdumpster_data = get_dnsdumpster_data(domain_name)
    print("\nDNSDumpster Data:")
    print(dnsdumpster_data)

    # MXToolbox data
    mxtoolbox_data = get_mxtoolbox_data(domain_name)
    print("\nMXToolbox Data:")
    print(mxtoolbox_data)

    # WHOXY data
    whoxy_data = get_whoxy_data(domain_name)
    print("\nWHOXY Data:")
    print(whoxy_data)

if __name__ == "__main__":
    main()
