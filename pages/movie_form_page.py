from random import randrange
import time
import allure
import resp as resp

from page_objects.page_objects import MovieFormObjects


class MovieFormPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening Submit Movie Form")
    def open_page(self):
        self.driver.get("https://sansmoviedb.com/movieform")

    @allure.step("Validate Field Limit")
    def validate_field_limit(self):
        # Obtain max value of movie title field
        maxlengthdefined = self.driver.find_element(*MovieFormObjects.text_movie_title_field)\
            .get_attribute("maxlength")
        # This movie value could replaced with a variable to read in csv data
        # and loop through several titles of various values
        self.driver.find_element(*MovieFormObjects.text_movie_title_field) \
            .send_keys("Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb")
        title = self.driver.find_element(*MovieFormObjects.text_movie_title_field) \
           .get_attribute("value")
        if len(title < maxlengthdefined):
            print("Movie title meets character limit requirement")
        elif len(title > maxlengthdefined):
            print("Movie title exceeds 200 character limit")
        else:
            print("Test conditions failed, review log for additional information")

    @allure.step("Validate Field Limit")
    def validate_date_input(self):
        start_timestamp = time.mktime(time.strptime('Jun 1 2010  01:33:00', '%b %d %Y %I:%M:%S'))
        end_timestamp: float = time.mktime(time.strptime('Jun 1 2017  12:33:00', '%b %d %Y %I:%M:%S'))
        release_date = time.strftime('%b %d %Y %I:%M:%S', time.localtime(randrange(start_timestamp, end_timestamp)))

        self.driver.find_element(*MovieFormObjects.text_rating_field).send_keys(release_date)
        verify_date = self.driver.find_element(*MovieFormObjects.text_rating_field).get_attribute("value")
        if verify_date >= "01/10/2015":
            print("Release date is within acceptable range")
        else:
            print("An invalid date has been entered")

    @allure.step("Validate Rating Range")
    def validate_rating_input(self):
        for x in range(0, 7):
            self.driver.find_element(*MovieFormObjects.text_rating_field).send_keys(x)
            if x in range(1, 6):
                print("Rating falls in range of 1 to 5")
            else:
                print("Rating is outside of range")

    @allure.step("Validate Button Default")
    def validate_button_default(self):
        if self.driver.find_element(*MovieFormObjects.btn_add_movie).get_property('disabled'):
            print("Default state of button is disabled")
        else:
            print("Button should be disabled until all fields have input")

    @allure.step("Validate Button Active")
    def validate_button_active(self):
        element = self.driver.find_element(*MovieFormObjects.btn_add_movie)
        self.driver.find_element(*MovieFormObjects.text_movie_title_field).send_keys("Top Gun: Maverick")
        self.driver.find_element(*MovieFormObjects.text_release_date_field).send_keys("11/19/2021")
        self.driver.find_element(*MovieFormObjects.text_rating_field).send_keys(1)
        if element.get_property('enabled'):
            element.click()
            if resp.status.code == 200:
                print("Movie has been submitted")
            else:
                print("Movie failed to submit")
        else:
            print("Button failed to enabled, check log for details")


