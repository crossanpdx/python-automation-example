from selenium.webdriver.common.by import By


class LogInObjects:
    user_account_menu = (By.CSS_SELECTOR, "#menu")
    login_link = (By.LINK_TEXT, "Login")
    logout_link = (By.LINK_TEXT, "Logout")
    email_input = (By.CSS_SELECTOR, "#email")
    password_input = (By.CSS_SELECTOR, "#password")


class MovieFormObjects:
    text_movie_title_field = (By.CSS_SELECTOR, "#title")
    text_release_date_field = (By.CSS_SELECTOR, "#date")
    text_rating_field = (By.CSS_SELECTOR, "rating")
    btn_add_movie = (By.CSS_SELECTOR, "button")
