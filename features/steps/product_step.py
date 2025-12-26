from behave import *
from pages.product_page import Product
import logging
@given('I am on the product page')
def user_on_product_page(context):
    context.on_product_page=Product(context.page)
    context.on_product_page.validate_products_page_loaded()
    logging.info('user on the product page...')

@then('User should see all products displayed')
def verify_all_products_displayed(context):
    context.on_product_page.verify_all_products_displayed()
    logging.info('all products displayed verified...')

@then('Each product should have an image')
def verify_product_images(context):
    context.on_product_page.verify_product_images()
    logging.info('product images verified...')

@then('Each product should have a title')
def verify_product_titles(context):
    context.on_product_page.verify_product_titles()
    logging.info('product titles verified...')

@then('Each product should have a price')
def verify_product_prices(context):
    context.on_product_page.verify_product_prices()
    logging.info('product prices verified...')

@then('Each product should have an "Add to cart" button')
def verify_add_to_cart_buttons(context):
    context.on_product_page.verify_add_to_cart_buttons()
    logging.info('add to cart buttons verified...')

@when('User clicks on sort dropdown')
def click_sort_dropdown(context):
    context.on_product_page.click_sort_dropdown()
    logging.info('sort dropdown clicked...')

@then('User should see following sort options')
def verify_sort_options(context):
    expected_options = [row[0] for row in context.table]
    context.on_product_page.verify_sort_options(expected_options)
    logging.info('sort options verified...')

@when('User selects a sort option')
def select_sort_option(context):
    context.on_product_page.select_sort_option()
    logging.info('sort option selected...')

@then('Products should be sorted accordingly')
def verify_products_sorted(context):
    context.on_product_page.verify_products_sorted()
    logging.info('products sorting verified...')

@when('User clicks on a product')
def click_on_product(context):
    context.on_product_page.click_on_product()
    logging.info('product clicked...')

@then('User should see detailed product information')
def verify_detailed_product_info(context):
    context.on_product_page.verify_detailed_product_info()
    logging.info('detailed product info verified...')

@then('User should see product description')
def verify_product_description(context):
    context.on_product_page.verify_product_description()
    logging.info('product description verified...')

@then('User should see product price')
def verify_product_price(context):
    context.on_product_page.verify_product_price()
    logging.info('product price verified...')

@then('User should see "Add to cart" button')
def verify_add_to_cart_button(context):
    context.on_product_page.verify_add_to_cart_button()
    logging.info('add to cart button verified...')
    