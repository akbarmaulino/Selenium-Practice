from behave import given, when, then
from selenium import webdriver

# Assuming you're using Selenium WebDriver for browser automation

@given('The User Already in The Youtube Music Login Page')
def user_already_in_login_page(context):
    context.driver = webdriver.Chrome()  # Inisialisasi browser
    context.driver.get("https://music.youtube.com/")  # Buka halaman login

@when('The User Not Fill {email} to Login')
def user_not_fill_email(context, email):
    # Di sini Anda akan menemukan elemen input untuk email dan password
    # Anda dapat menggunakan Selenium untuk mengakses elemen-elemen ini dan memasukkan email
    email_input = context.driver.find_element_by_xpath("//input[@name='email']")
    email_input.send_keys(email)

@then('The User can see error message that Email Or Password must be fill')
def user_sees_error_message(context):
    # Di sini Anda akan menemukan elemen tempat pesan kesalahan ditampilkan
    # Anda dapat menggunakan Selenium untuk mengonfirmasi bahwa pesan kesalahan sesuai dengan yang diharapkan
    error_message = context.driver.find_element_by_xpath("//div[@class='error-message']")
    assert error_message.text == "Email or Password must be filled", "Error message is not as expected"

# Anda mungkin perlu menambahkan langkah-langkah tambahan untuk menutup browser setelah skenario selesai

def close_browser(context):
    context.driver.quit()
