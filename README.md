Python.org News Scraper
A simple web scraper built with Selenium that extracts the latest news items from the Python.org homepage.
Description
This script automatically navigates to python.org, waits for the news section to load, and extracts the titles and links of all news items from the blog widget. It uses Selenium WebDriver with Chrome to perform the scraping.
Features

Automated Chrome browser control using Selenium
Automatic ChromeDriver installation and management via webdriver-manager
Explicit waits to ensure elements are loaded before scraping
Clean error handling with automatic browser cleanup
Optional headless mode for background execution

-----Prerequisites-----

Python 3.6 or higher
Google Chrome browser installed on your system

-----Installation-----

Clone or download this repository
Install the required dependencies:

bashpip install selenium webdriver-manager
Usage
Run the script using Python:
bashpython scraper.py
The script will:

Open Chrome browser
Navigate to https://www.python.org
Wait for news items to load (up to 10 seconds)
Print each news title and its corresponding link
Automatically close the browser

Example Output
Python 3.12.0 released -> https://www.python.org/downloads/release/python-3120/
PSF News: Community Updates -> https://pyfound.blogspot.com/...

-----Configuration-----

Headless Mode
To run the scraper without opening a visible browser window, uncomment this line in the code:
pythonchrome_options.add_argument("--headless")
Wait Time
The script waits up to 10 seconds for elements to load. You can adjust this timeout by changing the value in:
pythonWebDriverWait(driver, 10)  # Change 10 to your preferred timeout in seconds
How It Works

Driver Setup: Initializes Chrome WebDriver using webdriver-manager for automatic driver management
Page Navigation: Opens the Python.org homepage
Element Location: Uses CSS selectors to find news items in the blog widget
Explicit Wait: Waits for elements to be present before attempting to extract data
Data Extraction: Retrieves text content and href attributes from each news link
Cleanup: Ensures browser is closed even if errors occur

-----Dependencies-----

selenium: Web browser automation framework
webdriver-manager: Automatic management of browser drivers

-----Troubleshooting-----

Browser doesn't close: The script uses a finally block to ensure the browser closes even if an error occurs.
Elements not found: If the website structure changes, you may need to update the CSS selector .medium-widget.blog-widget li a.
Timeout errors: Increase the wait time if you have a slower internet connection.
Chrome version mismatch: webdriver-manager automatically handles ChromeDriver versions, but ensure your Chrome browser is up to date.
License

This project is open source and available for educational purposes.
