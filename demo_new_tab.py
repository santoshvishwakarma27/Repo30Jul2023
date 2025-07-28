#!/usr/bin/env python3
"""
Demo: Opening New Tabs in Selenium WebDriver
============================================

This script demonstrates the most practical ways to open new tabs in Selenium.
It uses webdriver-manager to automatically handle Chrome driver setup.

Run this script to see different tab opening methods in action.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_driver(headless=False):
    """
    Setup Chrome driver with automatic driver management
    """
    chrome_options = Options()
    
    if headless:
        chrome_options.add_argument("--headless")
    
    # Add other useful options
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Use webdriver-manager to automatically handle Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver


def demo_javascript_method():
    """
    Demo 1: Most reliable method using JavaScript
    """
    print("\n" + "="*50)
    print("DEMO 1: JavaScript Method (Recommended)")
    print("="*50)
    
    driver = setup_driver()
    
    try:
        # Navigate to initial page
        driver.get("https://httpbin.org/get")
        print(f"✓ Opened initial page: {driver.title}")
        time.sleep(2)
        
        # Store original window handle
        original_window = driver.current_window_handle
        print(f"✓ Original window handle: {original_window[:8]}...")
        
        # Open new blank tab using JavaScript
        driver.execute_script("window.open('');")
        print("✓ Executed JavaScript to open new tab")
        
        # Wait for new window and switch to it
        WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])
        print(f"✓ Switched to new tab: {driver.current_window_handle[:8]}...")
        
        # Navigate to different URL in new tab
        driver.get("https://httpbin.org/json")
        print(f"✓ Navigated to: {driver.current_url}")
        print(f"✓ New tab title: {driver.title}")
        time.sleep(2)
        
        # Switch back to original tab
        driver.switch_to.window(original_window)
        print(f"✓ Switched back to original tab: {driver.title}")
        
        print(f"✓ Total tabs open: {len(driver.window_handles)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")


def demo_direct_url_method():
    """
    Demo 2: Open new tab with URL directly
    """
    print("\n" + "="*50)
    print("DEMO 2: Direct URL Method")
    print("="*50)
    
    driver = setup_driver()
    
    try:
        # Navigate to initial page
        driver.get("https://httpbin.org/get")
        print(f"✓ Initial page: {driver.title}")
        time.sleep(1)
        
        # Open new tab with URL directly
        driver.execute_script("window.open('https://httpbin.org/uuid', '_blank');")
        print("✓ Opened new tab with direct URL")
        
        # Wait and switch to new tab
        WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])
        
        print(f"✓ New tab URL: {driver.current_url}")
        print(f"✓ New tab title: {driver.title}")
        print(f"✓ Total tabs: {len(driver.window_handles)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")


def demo_keyboard_method():
    """
    Demo 3: Keyboard shortcut method (Ctrl+T)
    """
    print("\n" + "="*50)
    print("DEMO 3: Keyboard Shortcut Method")
    print("="*50)
    
    driver = setup_driver()
    
    try:
        # Navigate to initial page
        driver.get("https://httpbin.org/get")
        print(f"✓ Initial page: {driver.title}")
        time.sleep(1)
        
        # Send Ctrl+T to open new tab
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.CONTROL + "t")
        print("✓ Sent Ctrl+T keyboard shortcut")
        
        # Wait for new tab and switch to it
        time.sleep(2)  # Give time for tab to open
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            print("✓ Switched to new tab")
            
            # Navigate to a URL
            driver.get("https://httpbin.org/status/200")
            print(f"✓ Navigated to: {driver.current_url}")
            print(f"✓ Total tabs: {len(driver.window_handles)}")
        else:
            print("⚠️  Keyboard shortcut didn't create new tab (this can happen)")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")


def demo_multiple_tabs():
    """
    Demo 4: Managing multiple tabs
    """
    print("\n" + "="*50)
    print("DEMO 4: Multiple Tabs Management")
    print("="*50)
    
    driver = setup_driver()
    
    try:
        # Start with initial page
        driver.get("https://httpbin.org/get")
        print(f"✓ Initial page: {driver.title}")
        time.sleep(1)
        
        # URLs to open in new tabs
        urls = [
            "https://httpbin.org/json",
            "https://httpbin.org/uuid", 
            "https://httpbin.org/status/200"
        ]
        
        # Open each URL in a new tab
        for i, url in enumerate(urls, 1):
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)
            print(f"✓ Tab {i+1}: {driver.current_url}")
            time.sleep(1)
        
        print(f"✓ Total tabs opened: {len(driver.window_handles)}")
        
        # Demonstrate switching between all tabs
        print("\n📋 Tab Summary:")
        for i, handle in enumerate(driver.window_handles):
            driver.switch_to.window(handle)
            print(f"   Tab {i+1}: {driver.current_url}")
        
        # Close all tabs except the first one
        print("\n🗂️  Closing extra tabs...")
        for handle in driver.window_handles[1:]:
            driver.switch_to.window(handle)
            driver.close()
            print("   ✓ Closed a tab")
        
        # Switch back to first tab
        driver.switch_to.window(driver.window_handles[0])
        print(f"✓ Remaining tab: {driver.current_url}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()
        print("✓ Browser closed")


def quick_example():
    """
    Quick example for copy-paste
    """
    print("\n" + "="*50)
    print("QUICK COPY-PASTE EXAMPLE")
    print("="*50)
    
    # This is the minimal code you need:
    driver = setup_driver()
    
    try:
        # Open initial page
        driver.get("https://www.google.com")
        
        # Open new tab
        driver.execute_script("window.open('');")
        
        # Switch to new tab
        driver.switch_to.window(driver.window_handles[-1])
        
        # Navigate in new tab
        driver.get("https://www.python.org")
        
        print("✓ Quick example completed successfully!")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    print("🚀 Selenium New Tab Demo")
    print("This demo shows different methods to open new tabs in Selenium WebDriver")
    
    try:
        # Run all demos
        demo_javascript_method()
        demo_direct_url_method()
        demo_keyboard_method()
        demo_multiple_tabs()
        quick_example()
        
        print("\n" + "="*50)
        print("🎉 ALL DEMOS COMPLETED SUCCESSFULLY!")
        print("="*50)
        print("\nMost Recommended Methods:")
        print("1. JavaScript: driver.execute_script(\"window.open('');\")")
        print("2. Direct URL: driver.execute_script(\"window.open('URL', '_blank');\")")
        print("3. Always use: driver.switch_to.window(driver.window_handles[-1])")
        
    except KeyboardInterrupt:
        print("\n\n❌ Demo interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Demo failed: {e}")
        print("Make sure Chrome browser is installed on your system")


# Additional utility functions for integration into existing code

def open_new_tab_simple(driver, url=None):
    """
    Simple utility function to open a new tab
    
    Args:
        driver: Selenium WebDriver instance
        url: Optional URL to navigate to in the new tab
    
    Returns:
        str: Window handle of the new tab
    """
    # Store current number of windows
    original_windows = driver.window_handles
    
    # Open new tab
    if url:
        driver.execute_script(f"window.open('{url}', '_blank');")
    else:
        driver.execute_script("window.open('');")
    
    # Wait for new window and get its handle
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > len(original_windows))
    new_window = [w for w in driver.window_handles if w not in original_windows][0]
    
    # Switch to new tab
    driver.switch_to.window(new_window)
    
    return new_window


def close_extra_tabs(driver, keep_first=True):
    """
    Close all tabs except optionally the first one
    
    Args:
        driver: Selenium WebDriver instance
        keep_first: Whether to keep the first tab open
    """
    tabs_to_close = driver.window_handles[1:] if keep_first else driver.window_handles[:]
    
    for handle in tabs_to_close:
        driver.switch_to.window(handle)
        driver.close()
    
    # Switch to remaining tab if any
    if driver.window_handles:
        driver.switch_to.window(driver.window_handles[0])