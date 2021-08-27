import pytest
import allure

from pages.movie_form_page import MovieFormPage


@pytest.mark.usefixtures("setup", "website_setup")
class TestAddMovieForm:

    @allure.title("Test Title Field Limit")
    @allure.description("string, 200 maximum characters")
    def test_title_field_limit(self, config):
        movie_form = MovieFormPage(self.driver)
        movie_form.open_page()
        movie_form.validate_field_limit()

    @allure.title("Test Release Date Field")
    @allure.description("date, greater than or equal to 1/10/2015")
    def test_release_date_field(self):
        movie_form = MovieFormPage(self.driver)
        movie_form.open_page()
        movie_form.validate_date_input()

    @allure.title("Test Rating Field")
    @allure.description("integer, 1 to 5")
    def test_rating_field(self):
        movie_form = MovieFormPage(self.driver)
        movie_form.open_page()
        movie_form.validate_rating_input()

    @allure.title("Test Add Movie Button")
    @allure.description("submits, default disabled unless required fields are satisfied")
    def test_add_movie_btn(self):
        movie_form = MovieFormPage(self.driver)
        movie_form.open_page()
        movie_form.validate_button_default()
        movie_form.validate_button_active()
