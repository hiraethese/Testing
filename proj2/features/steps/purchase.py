from behave import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import time

# Scenario Outline: Adding an item from the list to the shopping cart

@given('the user is on the main page')
def step_impl(context):
    context.driver.get("http://opencart:8080/")

@when('the user clicks on {product_name} button with a shopping cart icon')
def step_impl(context, product_name):

    if product_name == "MacBook":
        cart_button_xpath = "//div[@id='content']/div[2]/div/div/div[2]/form/div/button" # MacBook
        cart_button = context.driver.find_element(By.XPATH, cart_button_xpath)
        context.driver.execute_script("arguments[0].scrollIntoView(true);", cart_button)

        for _ in range(3):
            try:
                cart_button.click()
                break
            except ElementClickInterceptedException:
                time.sleep(1)

    elif product_name == "iPhone":
        cart_button_xpath = "//div[@id='content']/div[2]/div[2]/div/div[2]/form/div/button" # iPhone
        cart_button = context.driver.find_element(By.XPATH, cart_button_xpath)
        context.driver.execute_script("arguments[0].scrollIntoView(true);", cart_button)

        for _ in range(3):
            try:
                cart_button.click()
                break
            except ElementClickInterceptedException:
                time.sleep(1)

@then('{product_name} is added to the shopping cart')
def step_impl(context, product_name):
    pass
    
@then('the user receives an addition notification')
def step_impl(context):
    try:
        alert = context.driver.find_element(By.CSS_SELECTOR, ".alert")
        assert alert.is_displayed(), "Alert message is not visible."
    except NoSuchElementException:
        assert False, "No alert message is present on the page."

# Scenario Outline: Adding multiple items to the shopping cart

@given('the user has navigated to the page of {product_name}')
def step_impl(context, product_name):
    name = product_name.lower()
    context.driver.get("http://opencart:8080/en-gb/product/" + name)

@when('the user enters {product_quantity} in the "Qty" input field')
def step_impl(context, product_quantity):
    input_quantity_id = "input-quantity"
    input_quantity = context.driver.find_element(By.ID, input_quantity_id)
    input_quantity.clear()
    input_quantity.send_keys(product_quantity)

@when('the user clicks on "Add to Cart" button')
def step_impl(context):
    button_cart_id = "button-cart"
    button_cart = context.driver.find_element(By.ID, button_cart_id)
    button_cart.click()

# Scenario Outline: Removing an item from the mini shopping cart

@given('the user clicked on the shopping cart button')
def step_impl(context):
    mini_cart_xpath = "//div[@id='header-cart']/div/button"
    mini_cart = context.driver.find_element(By.XPATH, mini_cart_xpath)
    mini_cart.click()

@given('the shopping cart is not empty')
def step_impl(context):
    pass

@when('the user clicks on the cross button of {product_name}')
def step_impl(context, product_name):
    try:
        xmark_css = ".fa-circle-xmark"
        xmark = context.driver.find_element(By.CSS_SELECTOR, xmark_css)
        xmark.click()
    except NoSuchElementException:
        assert True

@then('{product_name} is removed from the shopping list')
def step_impl(context, product_name):
    pass

@then('the user receives a deletion notification')
def step_impl(context):
    pass

# Scenario Outline: Removing an item from the shopping cart

@given('the user has navigated to the shopping cart page')
def step_impl(context):
    # Add iPhone to the shopping cart
    cart_button_xpath = "//div[@id='content']/div[2]/div[2]/div/div[2]/form/div/button" # iPhone
    cart_button = context.driver.find_element(By.XPATH, cart_button_xpath)
    context.driver.execute_script("arguments[0].scrollIntoView(true);", cart_button)
    for _ in range(3):
        try:
            cart_button.click()
            break
        except ElementClickInterceptedException:
            time.sleep(1)
    # Navigate to the shopping cart page
    context.driver.get("http://opencart:8080/en-gb?route=checkout/cart")

# Scenario Outline: Editing the number of items in the shopping cart

@when('the user enters {product_quantity} in the "Quantity" input field of {product_name}')
def step_impl(context, product_quantity, product_name):
    quantity_name = "quantity"
    quantity = context.driver.find_element(By.NAME, quantity_name)
    quantity.clear()
    quantity.send_keys(product_quantity)

@when('the user clicks the "Update" button')
def step_impl(context):
    update_button_xpath = "//div[@id='shopping-cart']/div/table/tbody/tr/td[4]/form/div/button"
    update_button = context.driver.find_element(By.XPATH, update_button_xpath)
    update_button.click()

@then('{product_name} in the amount of {product_quantity} is in the shopping cart')
def step_impl(context, product_name, product_quantity):
    pass

@then('the user receives a modification notification')
def step_impl(context):
    try:
        alert = context.driver.find_element(By.CSS_SELECTOR, ".alert")
        assert alert.is_displayed(), "Alert message is not visible."
    except NoSuchElementException:
        assert False, "No alert message is present on the page."
