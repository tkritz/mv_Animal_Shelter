import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get email credentials from environment variables
YOUR_EMAIL = os.getenv('EMAIL_USER')
YOUR_PASSWORD = os.getenv('EMAIL_PASS')
TO_EMAIL = "ljunicity@gmail.com"
SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587

# Breeds to check for
desired_breeds = ["Maltipoo", "Maltese Poodle", "Maltese Poodle mix"]

def send_email(subject, message):
    msg = MIMEMultipart()
    msg["From"] = YOUR_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Set up Yahoo SMTP server and send the email
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(YOUR_EMAIL, YOUR_PASSWORD)
    text = msg.as_string()
    server.sendmail(YOUR_EMAIL, TO_EMAIL, text)
    server.quit()

# Set up Chrome options for Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL template to monitor (changing PAGE number dynamically)
url_template = "https://petharbor.com/results.asp?searchtype=ADOPT&start=3&friends=1&samaritans=1&nosuccess=0&orderby=Name&rows=10&imght=300&imgres=Detail&tWidth=200&view=sysadm.v_irvn&nobreedreq=1&bgcolor=D1D1D1&text=000000&link=ffffff&alink=fffff3&vlink=fffff6&fontface=arial&fontsize=12&col_hdr_bg=4196E1&col_hdr_fg=ffffff&col_bg=F6F6F6&col_bg2=ffffff&col_fg=black&SBG=F6F6F6&zip=92691&miles=10&shelterlist='MSVJ'&atype=&where=type_DOG&PAGE={page}"

# Iterate through multiple pages
found_breed = None
for page_num in range(1, 5):  # Checking first 4 pages (adjust as needed)
    url = url_template.format(page=page_num)
    
    driver.get(url)
    driver.implicitly_wait(10)
    
    page_content = driver.page_source
    
    # Check for the presence of any of the desired breeds
    for breed in desired_breeds:
        if breed.lower() in page_content.lower():
            found_breed = breed
            break

    if found_breed:
        break

driver.quit()

if found_breed:
    print(f"Found {found_breed}!")
    subject = f"Mission Viejo Animal Shelter - {found_breed} Available!"
    message = f"A {found_breed} is available for adoption! Check the details here: {url}"
    send_email(subject, message)
    print(f"Email sent about {found_breed}.")
else:
    print("No matching breeds found.")
