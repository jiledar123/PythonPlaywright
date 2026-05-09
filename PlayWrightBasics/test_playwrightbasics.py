import time

from playwright.async_api import Playwright
from playwright.sync_api import Page, expect


def test_invoke_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")


def test_invoke_browser_shortcut(page: Page):
    page.goto('https://rahulshettyacademy.com/client')


def test_core_locators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("")
    page.get_by_label("Password:").fill("")
    page.get_by_role("combobox").select_option(value="teach")
    page.get_by_role('button', name='Sign In').click()
    time.sleep(5)


def test_verify_invalid_login(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label('Username:').fill("")
    page.get_by_label('Password:').fill("")
    page.get_by_role("combobox").select_option(value="teach")
    page.get_by_role('checkbox').click()
    page.get_by_role('button', name='Sign In').click()
    expect(page.get_by_text('Incorrect username/password.')).to_be_visible()


def test_run_in_firefox(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    time.sleep(5)


def test_verify_add_to_cart(playwright):
    browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label('Username:').fill('')
    page.get_by_label('Password:').fill('')
    page.get_by_role('combobox').select_option(value='teach')
    page.get_by_role('checkbox').click()
    page.get_by_role('button', name='Sign In').click()
    iphone = page.locator('app-card').filter(has_text='iphone X')
    iphone.get_by_role('button').click()
    nokia = page.locator('app-card').filter(has_text='Nokia Edge')
    nokia.get_by_role('button').click()
    page.get_by_text('Checkout').click()
    expect(page.locator('.media-heading a').filter(has_text='iphone X')).to_be_visible()
    expect(page.locator('.media-heading a').filter(has_text='iphone X')).to_be_visible()
    time.sleep(5)


def test_handle_child_window(page: Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    # closer
    with page.expect_popup() as newPage_info:
        page.get_by_text('Free Access').click()
        child_page = newPage_info.value
        expect(child_page.locator('h1').filter(has_text='Documents request')).to_be_visible()


def test_show_hide(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role('button', name='Hide').click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


def test_handle_alert(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    page.get_by_placeholder('Enter Your Name').fill("Tester")
    page.on('dialog', lambda dialog : dialog.accept())
    page.get_by_role('button', name='Confirm').click()
    time.sleep(5)

def test_frames(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role('link', name= 'Mentorship').click()
    time.sleep(5)
#     extract the price of rice daynamically
def test_handle_webtable(page:Page):
    global price_column
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator('th').count()):
        if page.locator('th').nth(index).filter(has_text='Price').count()>0:
            price_column = index
            print(f'Column index of price is {price_column}')
            break
    rice_row = page.locator('tr').filter(has_text='Rice')
    expect(rice_row.locator('td').nth(price_column)).to_have_text('37')

def test_mouse_hover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Reload").click()
    

