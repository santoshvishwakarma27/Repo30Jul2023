"""
Selenium New Tab Examples - Quick Reference
===========================================

This file contains the most common and effective methods to open new tabs in Selenium WebDriver.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def method_1_javascript_blank_tab():
    """
    Method 1: Open blank new tab using JavaScript (Most Reliable)
    """
    driver = webdriver.Chrome()
    
    try:
        # Navigate to initial page
        driver.get("https://www.google.com")
        
        # Store original window handle
        original_window = driver.current_window_handle
        
        # Open new blank tab
        driver.execute_script("window.open('');")
        
        # Switch to new tab (it will be the last one in the list)
        driver.switch_to.window(driver.window_handles[-1])
        
        # Navigate to desired URL in new tab
        driver.get("https://www.python.org")
        
        # Switch back to original tab if needed
        driver.switch_to.window(original_window)
        
        print("Successfully opened new tab!")
        
    finally:
        driver.quit()


def method_2_javascript_with_url():
    """
    Method 2: Open new tab with URL directly using JavaScript
    """
    driver = webdriver.Chrome()
    
    try:
        # Navigate to initial page
        driver.get("https://www.google.com")
        
        # Open new tab with URL directly
        driver.execute_script("window.open('https://www.python.org', '_blank');")
        
        # Switch to new tab
        driver.switch_to.window(driver.window_handles[-1])
        
        print(f"New tab opened with title: {driver.title}")
        
    finally:
        driver.quit()


def method_3_keyboard_shortcut():
    """
    Method 3: Open new tab using Ctrl+T keyboard shortcut
    """
    driver = webdriver.Chrome()
    
    try:
        # Navigate to initial page
        driver.get("https://www.google.com")
        
        # Send Ctrl+T to open new tab
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + "t")
        
        # Switch to new tab
        driver.switch_to.window(driver.window_handles[-1])
        
        # Navigate to desired URL
        driver.get("https://www.github.com")
        
        print(f"New tab opened with title: {driver.title}")
        
    finally:
        driver.quit()


def method_4_ctrl_click_link():
    """
    Method 4: Open link in new tab using Ctrl+Click
    """
    driver = webdriver.Chrome()
    
    try:
        # Navigate to a page with links
        driver.get("https://www.google.com")
        
        # Find a link element (example: "Images" link)
        link = driver.find_element(By.LINK_TEXT, "Images")
        
        # Ctrl+Click to open in new tab
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        
        # Switch to new tab
        driver.switch_to.window(driver.window_handles[-1])
        
        print(f"Link opened in new tab: {driver.title}")
        
    finally:
        driver.quit()


def manage_multiple_tabs():
    """
    Example: Managing multiple tabs
    """
    driver = webdriver.Chrome()
    
    try:
        # Start with initial page
        driver.get("https://www.google.com")
        
        # List of URLs to open in new tabs
        urls = [
            "https://www.python.org",
            "https://www.github.com", 
            "https://stackoverflow.com"
        ]
        
        # Open each URL in a new tab
        for url in urls:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)
            print(f"Opened: {driver.title}")
        
        print(f"\nTotal tabs open: {len(driver.window_handles)}")
        
        # Switch between tabs
        for i, handle in enumerate(driver.window_handles):
            driver.switch_to.window(handle)
            print(f"Tab {i+1}: {driver.title}")
        
        # Close all tabs except the first one
        while len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
        
        # Switch back to first tab
        driver.switch_to.window(driver.window_handles[0])
        print(f"Remaining tab: {driver.title}")
        
    finally:
        driver.quit()


# Quick snippet for copy-paste
def quick_new_tab_snippet():
    """
    QUICK COPY-PASTE SNIPPET
    ========================
    """
    # Assuming you already have a driver instance
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    
    # Open new tab
    driver.execute_script("window.open('');")
    
    # Switch to new tab
    driver.switch_to.window(driver.window_handles[-1])
    
    # Navigate to URL in new tab
    driver.get("https://www.example.com")
    
    # Switch back to original tab (index 0)
    driver.switch_to.window(driver.window_handles[0])
    
    driver.quit()


if __name__ == "__main__":
    print("Testing different methods to open new tabs in Selenium...")
    
    print("\n1. JavaScript blank tab method:")
    method_1_javascript_blank_tab()
    
    print("\n2. JavaScript with URL method:")
    method_2_javascript_with_url()
    
    print("\n3. Keyboard shortcut method:")
    method_3_keyboard_shortcut()
    
    print("\n4. Managing multiple tabs:")
    manage_multiple_tabs()
    
    print("\nAll methods completed successfully!")


"""
SUMMARY OF METHODS:
==================

1. JavaScript (Recommended): driver.execute_script("window.open('');")
   - Most reliable across different browsers
   - Works consistently
   
2. Keyboard Shortcut: element.send_keys(Keys.CONTROL + "t")
   - Simulates user behavior
   - May not work in headless mode
   
3. Ctrl+Click: ActionChains with Ctrl+Click
   - Good for opening links in new tabs
   - Simulates natural user interaction

4. Direct URL: driver.execute_script("window.open('URL', '_blank');")
   - Opens tab with specific URL immediately
   - Fastest for known URLs

IMPORTANT NOTES:
================
- Always use driver.window_handles to get list of open tabs
- Use driver.switch_to.window(handle) to switch between tabs
- New tabs are typically added to the end of window_handles list
- Remember to close tabs when done: driver.close()
- Use driver.quit() to close all tabs and quit the browser
"""