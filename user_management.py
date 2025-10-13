HEAD
from playwright.sync_api import sync_playwright
import time

def test_user_management():
    with sync_playwright() as p:
        # Browser open
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Login
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)  # Wait for page to fully load
        page.fill('input[name="username"]', 'Admin')
        page.fill('input[name="password"]', 'admin123')
        page.click('button[type="submit"]')
        page.wait_for_selector("text=Dashboard")  # Wait for dashboard
        # Navigate to Admin - User Management - Users
        page.click('a[href*="admin"]')  # Admin menu
        page.wait_for_selector('//span[text()="User Management"]', timeout=5000)
        page.click('//span[text()="User Management"]')  # User Management tab
        page.wait_for_selector('//a[text()="Users"]', timeout=5000)
        page.click('//a[text()="Users"]')  # Users subtab
        time.sleep(1)
        # Add a new user
        page.click('//button[contains(text(),"Add")]')
        time.sleep(1)
        page.fill('input[name="username"]', 'testuser_123')
        page.fill('input[name="password"]', 'Testuser1011')
        page.fill('input[name="confirmPassword"]', 'Testuser1011')
        page.select_option('select[name="status"]', 'Enabled')
        page.click('//button[contains(text(),"Save")]')
        time.sleep(2)
        # Search for the user
        page.fill('input[placeholder="Username"]', 'Testuser_123')
        page.click('//button[contains(text(),"Search")]')
        time.sleep(1)
        # Edit user
        page.click('//button[contains(@class,"oxd-table-cell-actions") and contains(@title,"Edit")]')
        time.sleep(1)
        page.fill('input[name="username"]', 'TestUserUpdated')
        page.click('//button[contains(text(),"Save")]')
        time.sleep(2)
        # Validate updated user
        page.fill('input[placeholder="Username"]', 'TestUserUpdated')
        page.click('//button[contains(text(),"Search")]')
        time.sleep(1)
        # Delete user
        page.click('//button[contains(@class,"oxd-table-cell-actions") and contains(@title,"Delete")]')
        time.sleep(1)
        page.click('//button[text()=" Yes, Delete "]')
        time.sleep(2)
        browser.close()
if __name__ == "__main__":
    test_user_management()
from playwright.sync_api import sync_playwright
import time

def test_user_management():
    with sync_playwright() as p:
        # Browser open
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Login
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)  # Wait for page to fully load
        page.fill('input[name="username"]', 'Admin')
        page.fill('input[name="password"]', 'admin123')
        page.click('button[type="submit"]')
        page.wait_for_selector("text=Dashboard")  # Wait for dashboard
        # Navigate to Admin - User Management - Users
        page.click('a[href*="admin"]')  # Admin menu
        page.wait_for_selector('//span[text()="User Management"]', timeout=5000)
        page.click('//span[text()="User Management"]')  # User Management tab
        page.wait_for_selector('//a[text()="Users"]', timeout=5000)
        page.click('//a[text()="Users"]')  # Users subtab
        time.sleep(1)
        # Add a new user
        page.click('//button[contains(text(),"Add")]')
        time.sleep(1)
        page.fill('input[name="username"]', 'testuser_123')
        page.fill('input[name="password"]', 'Testuser1011')
        page.fill('input[name="confirmPassword"]', 'Testuser1011')
        page.select_option('select[name="status"]', 'Enabled')
        page.click('//button[contains(text(),"Save")]')
        time.sleep(2)
        # Search for the user
        page.fill('input[placeholder="Username"]', 'Testuser_123')
        page.click('//button[contains(text(),"Search")]')
        time.sleep(1)
        # Edit user
        page.click('//button[contains(@class,"oxd-table-cell-actions") and contains(@title,"Edit")]')
        time.sleep(1)
        page.fill('input[name="username"]', 'TestUserUpdated')
        page.click('//button[contains(text(),"Save")]')
        time.sleep(2)
        # Validate updated user
        page.fill('input[placeholder="Username"]', 'TestUserUpdated')
        page.click('//button[contains(text(),"Search")]')
        time.sleep(1)
        # Delete user
        page.click('//button[contains(@class,"oxd-table-cell-actions") and contains(@title,"Delete")]')
        time.sleep(1)
        page.click('//button[text()=" Yes, Delete "]')
        time.sleep(2)
        browser.close()
if __name__ == "__main__":
    test_user_management()
