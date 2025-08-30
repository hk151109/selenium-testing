import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    """Setup Chrome WebDriver with options"""
    options = Options()
    options.add_argument("--headless")  # Uncomment for headless mode (Jenkins)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service("C:\\Program Files\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_register_login_and_add_task(driver):
    """Full flow: register -> login -> add task -> verify task"""

    print("\n[STEP] Opening registration page...")
    driver.get("http://127.0.0.1:5000/register")

    username = f"user{int(time.time())}"  # unique username each run
    password = "testpass"

    print(f"[STEP] Registering new user: {username}")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "confirm_password").send_keys(password)
    driver.find_element(By.ID, "register-btn").click()

    time.sleep(1)

    print("[STEP] Redirecting to login page...")
    driver.get("http://127.0.0.1:5000/login")

    print(f"[STEP] Logging in as {username}...")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(1)

    print("[STEP] Adding a new task...")
    task_text = "Automated Task - Selenium"
    driver.find_element(By.ID, "task-input").send_keys(task_text)
    driver.find_element(By.ID, "add-task-btn").click()

    time.sleep(1)

    print("[STEP] Checking if task was added...")
    tasks = driver.find_elements(By.CLASS_NAME, "task-item")
    task_texts = [t.text for t in tasks]

    print(f"[DEBUG] Current tasks: {task_texts}")
    assert any(task_text in t for t in task_texts), "Task not found in task list"

    print("[SUCCESS] Test passed - Task added and verified!")


def test_admin_login_and_add_task(driver):
    """Quick check with default admin user"""
    print("\n[STEP] Logging in with default admin user...")
    driver.get("http://127.0.0.1:5000/login")

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(1)

    print("[STEP] Adding task as admin...")
    task_text = "Admin Task - Selenium"
    driver.find_element(By.ID, "task-input").send_keys(task_text)
    driver.find_element(By.ID, "add-task-btn").click()

    time.sleep(1)

    print("[STEP] Verifying task is present...")
    tasks = driver.find_elements(By.CLASS_NAME, "task-item")
    task_texts = [t.text for t in tasks]

    print(f"[DEBUG] Current tasks: {task_texts}")
    assert any(task_text in t for t in task_texts), "Admin task not found"

    print("[SUCCESS] Admin login + task test passed")
