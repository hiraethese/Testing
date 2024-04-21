from behave import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import re

# Background:

@given('the user is on the website')
def step_impl(context):
    context.driver.get("http://opencart:8080/")
    context.driver.execute_script("window.scrollTo(0, 0);")

# Scenario: Searching with empty search bar

@given('the user is on any page on the website')
def step_impl(context):
    context.driver.get("http://opencart:8080/")

@when('the user clicks the search button')
def step_impl(context):
    search_button_xpath = "//div[@id='search']/button"
    search_button = context.driver.find_element(By.XPATH, search_button_xpath)
    search_button.click()

@then('the user navigates to the search page')
def step_impl(context):
    current_url = context.driver.current_url
    search_page_url = "http://opencart:8080/index.php?route=product/search"
    assert search_page_url in current_url, "Expected to go to search page."

@then('the search results are empty')
def step_impl(context):
    content_p_xpath = "//div[@id='content']/p"
    try:
        content_p = context.driver.find_element(By.XPATH, content_p_xpath)
        contains_text = "There is no product that matches the search criteria."
        assert contains_text in content_p.text, "Expected no product message not found."
    except NoSuchElementException:
        assert False, "No element found with the provided XPath."

# Scenario Outline: Searching for a product by name

@when('the user enters {product_keyword} into the search bar')
def step_impl(context, product_keyword):
    search_input_xpath = "//div[@id='search']/input"
    search_input = context.driver.find_element(By.XPATH, search_input_xpath)
    search_input.clear()
    search_input.send_keys(product_keyword)

@then('products similar to {product_keyword} are displayed in the results')
def step_impl(context, product_keyword):
    links_xpath = "//div[@id='product-list']//a"
    links = context.driver.find_elements(By.XPATH, links_xpath)
    if not links:
        content_p_xpath = "//div[@id='content']/p"
        try:
            content_p = context.driver.find_element(By.XPATH, content_p_xpath)
            contains_text = "There is no product that matches the search criteria."
            assert contains_text in content_p.text, "Expected no product message not found."
        except NoSuchElementException:
            assert False, "No element found with the provided XPath."
    else:
        failed_links = [link.text for link in links if link.text and product_keyword.lower() not in link.text.lower()]
        assert not failed_links, "There are links without a keyword."

# Scenario Outline: Applying search criteria to search results

@given('the user has navigated to the search page')
def step_impl(context):
    context.driver.get("http://opencart:8080/index.php?route=product/search")

@when('the user enters {product_keyword} into keywords')
def step_imp(context, product_keyword):
    keyword_input_xpath = "//div[@id='content']/div[2]/div/input"
    keyword_input = context.driver.find_element(By.XPATH, keyword_input_xpath)
    keyword_input.clear()
    keyword_input.send_keys(product_keyword)

@when('the user clicks on "All Categories"')
def step_impl(context):
    pass

@when('the user selects the {product_category} from the menu that appears')
def step_impl(context, product_category):
    dropdown_id = "input-category"
    dropdown = Select(context.driver.find_element(By.ID, dropdown_id))
    pattern = re.compile(product_category)
    for option in dropdown.options:
        if pattern.search(option.text):
            dropdown.select_by_visible_text(option.text)
            return
    raise AssertionError("No option was found that matches this product category")

@when('the user submits the search')
def step_impl(context):
    button_search_id = "button-search"
    button_search = context.driver.find_element(By.ID, button_search_id)
    button_search.click()

@then('products in the results from the {product_category} category')
def step_impl(context, product_category):
    pass

# Scenario Outline: Searching in product descriptions

@when('the user checks the box "Search in product descriptions"')
def step_impl(context):
    input_description_id = "input-description"
    input_description = context.driver.find_element(By.ID, input_description_id)
    input_description.click()

@then('products are displayed in the results')
def step_impl(context):
    pass

@then('the product descriptions contain the keyword {product_keyword}')
def step_impl(context, product_keyword):
    pass

# Scenario Outline: Searching in product descriptions and subcategories

@when('the user checks the box "Search in subcategories"')
def step_impl(context):
    input_sub_category_id = "input-sub-category"
    input_sub_category = context.driver.find_element(By.ID, input_sub_category_id)
    input_sub_category.click()

@then('similar products are displayed in the results')
def step_impl(context):
    pass

@then('the product category is a subcategory of the {product_category} category')
def step_impl(context, product_category):
    pass
