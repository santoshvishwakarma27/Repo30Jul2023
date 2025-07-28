# Selenium New Tab Guide

This guide provides comprehensive examples for opening new tabs in Selenium WebDriver with Python.

## 📁 Files in this Project

- `Sel/test_new_tab.py` - Comprehensive test class with multiple methods
- `selenium_new_tab_examples.py` - Quick reference with practical examples
- `demo_new_tab.py` - Interactive demo script with automatic driver management
- `requirements.txt` - Required Python packages

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install selenium webdriver-manager
```

### 2. Run the Demo

```bash
python demo_new_tab.py
```

## 📋 Methods Overview

### Method 1: JavaScript (Recommended) ⭐

**Most reliable method across different browsers and environments.**

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Open new blank tab
driver.execute_script("window.open('');")

# Switch to new tab
driver.switch_to.window(driver.window_handles[-1])

# Navigate to desired URL
driver.get("https://www.python.org")

driver.quit()
```

### Method 2: JavaScript with Direct URL

**Opens a new tab and navigates to URL in one step.**

```python
# Open new tab with URL directly
driver.execute_script("window.open('https://www.python.org', '_blank');")

# Switch to new tab
driver.switch_to.window(driver.window_handles[-1])
```

### Method 3: Keyboard Shortcut (Ctrl+T)

**Simulates user behavior but may not work in headless mode.**

```python
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Send Ctrl+T to open new tab
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.CONTROL + "t")

# Switch to new tab
driver.switch_to.window(driver.window_handles[-1])
```

### Method 4: Ctrl+Click on Links

**Opens links in new tabs by simulating Ctrl+Click.**

```python
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Find a link
link = driver.find_element(By.LINK_TEXT, "Some Link")

# Ctrl+Click to open in new tab
ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

# Switch to new tab
driver.switch_to.window(driver.window_handles[-1])
```

## 🛠️ Complete Example with Error Handling

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def open_new_tab_safely(driver, url=None):
    """
    Safely open a new tab with proper error handling
    """
    try:
        # Store current windows
        original_windows = driver.window_handles
        
        # Open new tab
        if url:
            driver.execute_script(f"window.open('{url}', '_blank');")
        else:
            driver.execute_script("window.open('');")
        
        # Wait for new window to appear
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > len(original_windows)
        )
        
        # Find and switch to new window
        new_window = [w for w in driver.window_handles if w not in original_windows][0]
        driver.switch_to.window(new_window)
        
        return new_window
        
    except Exception as e:
        print(f"Error opening new tab: {e}")
        return None

# Usage
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

# Open new tab
new_tab_handle = open_new_tab_safely(driver, "https://www.python.org")

if new_tab_handle:
    print("New tab opened successfully!")
    print(f"Current URL: {driver.current_url}")

driver.quit()
```

## 🔄 Managing Multiple Tabs

```python
def manage_multiple_tabs():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    
    # URLs to open
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
    
    print(f"Total tabs: {len(driver.window_handles)}")
    
    # Switch between tabs
    for i, handle in enumerate(driver.window_handles):
        driver.switch_to.window(handle)
        print(f"Tab {i+1}: {driver.current_url}")
    
    # Close all tabs except first
    while len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
    
    # Switch back to first tab
    driver.switch_to.window(driver.window_handles[0])
    
    driver.quit()
```

## 💡 Best Practices

### 1. Always Use Window Handles
```python
# ✅ Good
driver.switch_to.window(driver.window_handles[-1])

# ❌ Avoid hardcoded indices
# driver.switch_to.window("some-hardcoded-handle")
```

### 2. Wait for New Windows
```python
# ✅ Good - Wait for new window
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

# ❌ Avoid - No waiting
# time.sleep(1)  # Unreliable
```

### 3. Handle Exceptions
```python
try:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
except Exception as e:
    print(f"Failed to open new tab: {e}")
```

### 4. Clean Up Tabs
```python
# Close extra tabs when done
for handle in driver.window_handles[1:]:
    driver.switch_to.window(handle)
    driver.close()

# Return to main tab
driver.switch_to.window(driver.window_handles[0])
```

## 🔧 Utility Functions

```python
def open_new_tab(driver, url=None):
    """Open new tab and optionally navigate to URL"""
    original_windows = driver.window_handles
    
    if url:
        driver.execute_script(f"window.open('{url}', '_blank');")
    else:
        driver.execute_script("window.open('');")
    
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > len(original_windows))
    new_window = [w for w in driver.window_handles if w not in original_windows][0]
    driver.switch_to.window(new_window)
    return new_window

def close_all_tabs_except_first(driver):
    """Close all tabs except the first one"""
    for handle in driver.window_handles[1:]:
        driver.switch_to.window(handle)
        driver.close()
    driver.switch_to.window(driver.window_handles[0])

def switch_to_tab(driver, index):
    """Switch to tab by index (0-based)"""
    if 0 <= index < len(driver.window_handles):
        driver.switch_to.window(driver.window_handles[index])
        return True
    return False
```

## 🎯 Common Use Cases

### Opening Multiple URLs for Comparison
```python
urls = ["https://site1.com", "https://site2.com", "https://site3.com"]

for url in urls:
    open_new_tab(driver, url)
    # Do something with each site
    time.sleep(2)
```

### Testing Links in New Tabs
```python
links = driver.find_elements(By.TAG_NAME, "a")

for link in links[:3]:  # Test first 3 links
    href = link.get_attribute("href")
    if href:
        open_new_tab(driver, href)
        # Test the page
        assert "Expected Title" in driver.title
        driver.close()  # Close the tab
        driver.switch_to.window(driver.window_handles[0])  # Back to main
```

## 🐛 Troubleshooting

### Issue: New tab doesn't open
- **Cause**: Browser blocking popups
- **Solution**: Use Chrome options to disable popup blocking
```python
chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(options=chrome_options)
```

### Issue: Can't switch to new tab
- **Cause**: Race condition - tab not ready
- **Solution**: Use WebDriverWait
```python
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
```

### Issue: Wrong tab selected
- **Cause**: Assuming tab order
- **Solution**: Store and use specific window handles
```python
original_window = driver.current_window_handle
# ... open new tab ...
new_windows = [w for w in driver.window_handles if w != original_window]
driver.switch_to.window(new_windows[0])
```

## 📊 Method Comparison

| Method | Reliability | Browser Support | Headless Mode | Speed |
|--------|-------------|-----------------|---------------|-------|
| JavaScript | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Ctrl+T | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Ctrl+Click | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation**: Use JavaScript method for most reliable results.

## 🎮 Running the Examples

### Run Individual Tests
```bash
# Run pytest tests
python -m pytest Sel/test_new_tab.py -v

# Run specific test
python -m pytest Sel/test_new_tab.py::TestNewTab::test_open_new_tab_with_javascript -v
```

### Run Interactive Demo
```bash
python demo_new_tab.py
```

### Run Quick Examples
```bash
python selenium_new_tab_examples.py
```

---

## 📝 Summary

The **JavaScript method** (`driver.execute_script("window.open('');")`) is the most reliable way to open new tabs in Selenium. Always remember to:

1. Use `driver.window_handles` to manage tabs
2. Use `driver.switch_to.window()` to switch between tabs
3. Wait for new windows to appear before switching
4. Handle exceptions gracefully
5. Clean up tabs when done

Happy testing! 🚀