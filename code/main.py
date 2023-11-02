from selenium import webdriver
import time

import re

import os

url = "https://www.real.discount/udemy-coupon-code/"

# Initialize a webdriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Wait for the page to load completely (you can adjust the time as needed)
driver.implicitly_wait(10)

# Wait for an additional 10 minutes
time.sleep(5)

# Get the content after JavaScript execution
dynamic_content = driver.page_source
# Save dynamic_content to a text file
with open('code/text.txt', 'w', encoding='utf-8') as file:
    file.write(dynamic_content)

# Append additional text to the file
# with open('dynamic_content.txt', 'a', encoding='utf-8') as file:
#     file.write('\nappended text = dynamic_content')
# Close the browser
driver.quit()



# Now 'dynamic_content' contains the HTML after JavaScript execution
# You can parse it using BeautifulSoup or other methods if needed

# the code3 which is extracting data from html site ends here##################################################################################
 
# Part 1: Extract links from html.txt and write to link.txt
with open('code/text.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

matches = re.findall(r'<a.*?href=[\'"](.*?/offer/.*?)["\']', html_content)

with open('code/text.txt', 'w', encoding='utf-8') as file:
    for match in matches:
        file.write(match + '\n')

# Part 2: Remove '/offer/`+ item[' from link.txt
with open('code/text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

cleaned_links = [line.replace('/offer/`+ item[', '') for line in lines]

with open('code/text.txt', 'w', encoding='utf-8') as file:
    file.writelines(cleaned_links)

# the link.py which is use to write link like /offer/ ends here ######################################################################

# Specify the file path
# file_path = 'test.txt'

# # Check if the file exists before attempting to delete it
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f'{file_path} has been deleted.')
# else:
#     print(f'{file_path} does not exist.')



# Read links from link.txt
with open('code/text.txt', 'r', encoding='utf-8') as file:
    links = file.readlines()

# Initialize a webdriver (e.g., Chrome)
driver = webdriver.Chrome()

all_contant = ''  # Initialize all_contant before the loop

for url in links:
    # Construct the full URL
    full_url = "https://www.real.discount/" + url.strip()

    # Navigate to the URL
    driver.get(full_url)

    # Wait for the page to load completely (you can adjust the time as needed)
    driver.implicitly_wait(10)

    # Wait for an additional 3 seconds (if needed)
    time.sleep(3)

    # Get the content after JavaScript execution
    dynamic_content = driver.page_source
    all_contant += dynamic_content  # Concatenate the dynamic content

# Save dynamic_content to a text file
#with open('test.txt', 'w', encoding='utf-8') as file:
with open('code/text.txt', 'w', encoding='utf-8') as file:
    file.write(all_contant + '\n')

# Close the browser
driver.quit()


# the udlink.py which is use to join remaining link with /offer/ and jump to course link and extract each html page ######################

# Part 1: Extract links from html.txt and write to link.txt
with open('code/text.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

matches = re.findall(r'<a.*?href=[\'"](.*?udemy.com/course.*?)["\']', html_content)

with open('code/text.txt', 'w', encoding='utf-8') as file:
    for match in matches:
        # Remove text before "https://www.udemy.com/course"
        cleaned_match = re.sub(r'^.*https://www.udemy.com/course', 'https://www.udemy.com/course', match)
        file.write(cleaned_match + '\n')

#the udlink.py which is use to extract udemy.com main course link for last sand link ends here #######################################