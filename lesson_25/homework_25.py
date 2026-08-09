'''
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
Використовувати функцію text(), пошук за атрибутом @, та складні локатори (більш ніж з одним елементом)
'''

class HomePageLocators:
    guest_login_btn_xpath = "//button[text()='Guest log in']"
    guest_login_btn_css = "button.header-link.-guest"

    sign_in_btn_xpath = "//button[text()='Sign In']"
    sign_in_btn_css = "button.header_signin"

    do_more_title_xpath = "//h1[@class='hero-descriptor_title display-2']"
    do_more_title_css = ".display-2"

    sign_up_btn_xpath = "//button[@class='hero-descriptor_btn btn btn-primary']"
    sign_up_btn_css = ".hero-descriptor_btn.btn"

    p_sub_title_xpath = "//p[contains(text(), 'With the help of the Hillel')]"
    p_sub_title_css = ".hero-descriptor_descr.lead"

    log_fuel_expenses_xpath = "//p[@class='about-block_title h2' and text()='Log fuel expenses']"
    log_fuel_expenses_css = ".col-12:first-child .about-block_title"

    instructions_and_manuals_xpath = "//p[@class='about-block_title h2' and text()='Instructions and manuals']"
    instructions_and_manuals_css = ".col-12:nth-child(2) .about-block_title"

    keep_track_xpath = ("//p[@class='about-block_descr lead' and text()='Keep track of your replacement schedule and plan "
                  "your vehicle maintenance expenses in advance.']")
    keep_track_css = ".col-12:first-child .about-block_descr"

    watch_over_xpath = "//div//p[text()='Watch over 100 instructions and repair your car yourself.']"
    watch_over_css = ".col-12:nth-child(2) .about-block_descr"

    contacts_heading_xpath = "//h2[text()='Contacts']"
    contacts_heading_css = "div.col-md-6.d-flex > h2"

    fb_link_xpath = "//div//a//span[@class='socials_icon icon icon-facebook']"
    fb_link_css = ".icon-facebook"

    tel_link_xpath = "//h2[text()='Contacts']/following-sibling::div//a[contains(@href, 't.me')]"
    tel_link_css = ".icon-telegram"

    yt_link_xpath = "//div[@id='contactsSection']//a[contains(@href, 'youtube.com')]"
    yt_link_css = ".icon-youtube"

    instagram_link_xpath = "//div[contains(@class, 'contacts_socials')]/a[contains(@href, 'instagram')]"
    instagram_link_css = ".icon-instagram"

    in_link_xpath = "//a[span[contains(@class, 'icon-linkedin')]]"
    in_link_css = ".icon-linkedin"

    ithillel_logo_xpath = "//div[contains(@class, 'col-md-6')]/a[contains(@href, 'ithillel.ua')]"
    ithillel_logo_css = "a[href*='ithillel.ua']"

    support_email_link_xpath = "//a[text()='support@ithillel.ua']"
    support_email_link_css = "a[href^='mailto:']"

    header_logo_xpath = "//div//a[@class='header_logo']"
    header_logo_css = "a.header_logo"

    header_home_xpath = "//a[text()='Home']"
    header_home_css = "nav > a[href='/']"

    header_about_xpath = "//button[text()='About']"
    header_about_css = "button[appscrollto='aboutSection']"

    header_contacts_xpath = "//button[text()='Contacts']"
    header_contacts_css = "button[appscrollto='contactsSection']"

    footer_logo_xpath = "//div//a[@class='footer_logo']"
    footer_logo_css = ".footer_logo"

    footer_year_xpath = "(//app-footer//p)[1]"
    footer_year_css = ".footer_item > p:first-child"

    footer_description_xpath = "(//app-footer//p)[2]"
    footer_description_css = "footer p:last-child"

    youtube_block_xpath = "//iframe[contains(@src, 'youtube')]"
    youtube_block_css = "iframe[src*='youtube']"
