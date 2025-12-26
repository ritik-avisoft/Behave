from behave import *
from pages.login_page import login
from utils.test_data import Test_data as td
from pages.product_page import Product
import logging

@given('I am on the login page')
def user_on_login_page(context):
    context.on_login=login(context.page)
    context.on_login.on_login_page()
    logging.info('user on the login page...')

@given('User on the login page')
def user_on_login_page_alt(context):
    context.on_login=login(context.page)
    context.on_login.on_login_page()
    logging.info('user on the login page...')
    
@when('"{user_name}" user enter correct login credentials')
def user_enter_credential(context,user_name):
    context.on_login.logged_in(user_name,td.PASSWORD_ENCRYPTED)
    logging.info(f'{user_name} user logged in successfully...')

@when('If "{user_name}" user enter correct login credentials')
def user_enter_credential(context,user_name):
    context.on_login.locked_user_login(user_name,td.PASSWORD_ENCRYPTED)
    logging.info(f'{user_name} has been locked out...')

@then('User should see a locked out error message')
def verify_locked_out_error_message(context):
    context.on_login.locked_user_error_message()
    logging.info('locked out error message verified...')

@when('"{user_name}" user enter valid username and incorrect password')
def user_enter_invalid_password(context,user_name):
    context.on_login.incorrect_login(user_name )
    logging.info('user entered invalid password...')

@then('User should see an error message')
def verify_error_message(context):
    context.on_login.verify_login_error_message()
    logging.info('error message verified...')

@then('User should be on product page')
def verify_product_page(context):
    context.on_product_page=Product(context.page)
    context.on_product_page.validate_products_page_loaded()
    logging.info('product page verified...')


@when('I keep username and password blank')
def user_enters_blank_credentials(context):
    context.on_login.login_with_blank_credentials()
    logging.info('user entered blank credentials...')

@when('I keep blank username and fill valid password')
def user_enters_blank_username(context):
    context.on_login.login_with_blank_username(td.PASSWORD_ENCRYPTED)
    logging.info('user entered blank username...')

@when('I filled valid username and invalid password')
def user_enters_invalid_password(context):
    context.on_login.login_with_invalid_password("standard")
    logging.info('user entered invalid password...')

@then('User should see error message for blank credentials')
def verify_blank_credentials_error(context):
    context.on_login.verify_blank_credentials_error()
    logging.info('blank credentials error verified...')

@then('User should see error message for blank username')
def verify_blank_username_error(context):
    context.on_login.verify_blank_username_error()
    logging.info('blank username error verified...')

@then('User should see error message for invalid credentials')
def verify_invalid_credentials_error(context):
    context.on_login.verify_login_error_message()
    logging.info('invalid credentials error verified...')

