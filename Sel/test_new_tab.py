from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestNewTab:
    """
    Test class demonstrating different methods to open new tabs in Selenium
    """
    
    def setup_method(self):
        """Setup method to initialize the driver before each test"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
    
    def teardown_method(self):
        """Teardown method to close the driver after each test"""
        self.driver.quit()
    
    def test_open_new_tab_with_javascript(self):
        """Method 1: Open new tab using JavaScript"""
        # Navigate to initial page
        self.driver.get("https://www.google.com")
        print(f"Initial tab title: {self.driver.title}")
        
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Open new tab using JavaScript
        self.driver.execute_script("window.open('');")
        
        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        # Navigate to a different URL in the new tab
        self.driver.get("https://www.python.org")
        print(f"New tab title: {self.driver.title}")
        
        # Switch back to original tab
        self.driver.switch_to.window(original_window)
        print(f"Back to original tab: {self.driver.title}")
        
        # Demonstrate working with both tabs
        print(f"Total tabs open: {len(self.driver.window_handles)}")
    
    def test_open_new_tab_with_keys(self):
        """Method 2: Open new tab using keyboard shortcut (Ctrl+T)"""
        # Navigate to initial page
        self.driver.get("https://www.google.com")
        print(f"Initial tab title: {self.driver.title}")
        
        # Find body element and send Ctrl+T to open new tab
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.CONTROL + "t")
        
        # Wait a moment for the new tab to open
        time.sleep(1)
        
        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        # Navigate to a URL in the new tab
        self.driver.get("https://www.github.com")
        print(f"New tab title: {self.driver.title}")
        
        print(f"Total tabs open: {len(self.driver.window_handles)}")
    
    def test_open_link_in_new_tab(self):
        """Method 3: Open link in new tab using Ctrl+Click"""
        # Navigate to a page with links
        self.driver.get("https://www.google.com")
        
        # Search for something to get links
        search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("selenium python")
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results and find first link
        first_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3")))
        
        # Ctrl+Click to open in new tab
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).click(first_link).key_up(Keys.CONTROL).perform()
        
        # Wait a moment for the new tab to open
        time.sleep(2)
        
        print(f"Total tabs open: {len(self.driver.window_handles)}")
        
        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print(f"New tab title: {self.driver.title}")
    
    def test_multiple_tabs_management(self):
        """Method 4: Managing multiple tabs"""
        # Start with Google
        self.driver.get("https://www.google.com")
        original_window = self.driver.current_window_handle
        
        # Open multiple new tabs
        urls = [
            "https://www.python.org",
            "https://www.github.com",
            "https://stackoverflow.com"
        ]
        
        for url in urls:
            # Open new tab
            self.driver.execute_script("window.open('');")
            # Switch to new tab
            self.driver.switch_to.window(self.driver.window_handles[-1])
            # Navigate to URL
            self.driver.get(url)
            print(f"Opened tab with title: {self.driver.title}")
        
        print(f"Total tabs opened: {len(self.driver.window_handles)}")
        
        # Demonstrate switching between tabs
        for i, window_handle in enumerate(self.driver.window_handles):
            self.driver.switch_to.window(window_handle)
            print(f"Tab {i+1}: {self.driver.title}")
        
        # Close all tabs except the first one
        for window_handle in self.driver.window_handles[1:]:
            self.driver.switch_to.window(window_handle)
            self.driver.close()
        
        # Switch back to the original tab
        self.driver.switch_to.window(original_window)
        print(f"Remaining tab: {self.driver.title}")
    
    def test_open_new_tab_and_handle_windows(self):
        """Method 5: Advanced window handling with explicit tab opening"""
        # Navigate to initial page
        self.driver.get("https://www.google.com")
        print(f"Initial tab title: {self.driver.title}")
        
        # Store all current window handles
        original_windows = self.driver.window_handles
        
        # Open new tab with specific URL directly
        self.driver.execute_script("window.open('https://www.selenium.dev', '_blank');")
        
        # Wait for new window to appear
        self.wait.until(lambda driver: len(driver.window_handles) > len(original_windows))
        
        # Find the new window handle
        new_window = [window for window in self.driver.window_handles if window not in original_windows][0]
        
        # Switch to new tab
        self.driver.switch_to.window(new_window)
        print(f"New tab title: {self.driver.title}")
        
        # Verify we're on the correct page
        assert "Selenium" in self.driver.title
        
        print(f"Successfully opened and navigated to new tab!")


# Standalone function examples for quick reference
def open_new_tab_example():
    """Standalone example showing how to open a new tab"""
    driver = webdriver.Chrome()
    
    try:
        # Go to initial page
        driver.get("https://www.google.com")
        print("Original page:", driver.title)
        
        # Method 1: JavaScript approach (recommended)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.python.org")
        print("New tab:", driver.title)
        
        # Switch back to original tab
        driver.switch_to.window(driver.window_handles[0])
        print("Back to original:", driver.title)
        
    finally:
        driver.quit()


def open_multiple_tabs_example():
    """Example showing how to open and manage multiple tabs"""
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://www.google.com")
        
        # Open 3 new tabs
        for i in range(3):
            driver.execute_script("window.open('');")
        
        # Navigate to different URLs in each tab
        urls = ["https://www.python.org", "https://www.github.com", "https://stackoverflow.com"]
        
        for i, url in enumerate(urls, 1):
            driver.switch_to.window(driver.window_handles[i])
            driver.get(url)
            print(f"Tab {i}: {driver.title}")
        
        print(f"Total tabs: {len(driver.window_handles)}")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    # Run standalone examples
    print("=== Opening New Tab Example ===")
    open_new_tab_example()
    
    print("\n=== Multiple Tabs Example ===")
    open_multiple_tabs_example()