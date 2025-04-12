# MV Animal Shelter Breed Checker
 
This Python project was created for my mom, to automate the process of monitoring the **Mission Viejo Animal Shelter** website for specific dog breeds, such as **Maltese Poodle** or **Maltipoo**. When a desired breed is found, an email notification is sent automatically, ensuring that she never misses out on the chance to adopt a dog of her preferred breed.

## Features

- **Automated Breed Monitoring**: The script checks for specific breeds such as **Maltese Poodle**, **Maltipoo**, and **German Shepherd**, on the animal shelter's website.
- **Scheduled Execution**: The script is scheduled to run at specific intervals using GitHub Actions, eliminating the need for manual execution.
- **Email Notifications**: Sends an email to notify you when the specified breed becomes available at the shelter.
  
## How It Works

1. **Web Scraping**: The script uses Selenium to scrape the **Mission Viejo Animal Shelter** website for available dogs.
2. **Breed Check**: It searches the scraped content for specific breeds, including *Maltese Poodle*, *Maltipoo*, and *German Shepherd*.
3. **Email Alert**: If a matching breed is found, the script sends an email alert with details about the breed and a link to the shelter's website.

## Tech Stack

- **Python**: Core scripting language.
- **Selenium**: Used for web scraping.
- **SMTP (Yahoo Mail)**: Sends email alerts via Yahoo's SMTP server.
- **GitHub Actions**: Used to schedule the script at regular intervals.

## Prerequisites

Before you can run this script, you need to have the following installed:

- Python 3.x
- Google Chrome (for Selenium)
- The following Python libraries:
  - `selenium`
  - `webdriver-manager`
  - `smtplib`
  - `schedule`
  
To install the necessary dependencies, you can use the `requirements.txt` file:

```bash
pip install -r requirements.txt
