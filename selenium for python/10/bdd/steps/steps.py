from behave import *


@given('I am on home page')
def step_i_am_on_home_page(context):
    context.driver.get("https://www.amazon.com/")
    
@when('I search for {text}')
def step_i_search_for(context, text):
    search_field = context.driver.find_element_by_name("field-keywords")
    search_field.clear()
    
    search_field.send_keys(text)
    search_field.submit()
    
@then('I should see results {text} in search results')
def step_i_should_see_results(context, text):
    products = context.driver.find_elements_by_xpath("//div[@class='a-row s-result-list-parent-container']/ul/li")
    assert len(products) >= int(text)