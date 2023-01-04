import requests
from bs4 import BeautifulSoup

# Set the URL and the payload
url = 'https://en.numista.com/connexion/connecter.php'
payload = {'connexion_pseudo': 'stancollectsbot', 'connexion_mdp': '********', 'remember': 'on'} # Password Censored

# Make the request to the login page
response = requests.post(url, data=payload)

# Parse the response HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find the form element
form = soup.find('form', {'class': 'form'})

# Find all the input elements in the form
input_elements = form.find_all('input')

# Extract the form action and the csrf token
form_action = form['action']
csrf_token = form.find('input', {'name': 'csrf_token'})['value']

# Set the form action and the csrf token in the payload
payload['csrf_token'] = csrf_token
payload['action'] = form_action

# Add all the input elements to the payload
for element in input_elements:
    name = element['name']
    value = element['value']
    payload[name] = value

# Make the request to the login form action
response = requests.post(form_action, data=payload)

# Check the response status code
if response.status_code == 200:
    print('Successfully logged in!')
else:
    print('Failed to log in.')
