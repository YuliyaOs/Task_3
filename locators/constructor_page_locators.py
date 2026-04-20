from selenium.webdriver.common.by import By

make_burger_header = [By.XPATH, ".//h1[text()='Соберите бургер']"]
burger_ingredient = [
    By.XPATH, "(.//a[contains(@class,'BurgerIngredient')])[1]"]
ingredient_details = [By.XPATH, ".//h2[text()='Детали ингредиента']"]
close_details_button = [
    By.XPATH, "(.//button[contains(@type,'button')])[1]"]
modal_with_details = [
    By.XPATH, ".//section[contains(@class,'P3_V5')]"]
count_ingredient = [
    By.XPATH, "(.//p[contains(@class,'counter')])[1]"]
basket = [
    By.XPATH, ".//ul[contains(@class,'BurgerConstructor')]"]
place_order_button = [By.XPATH, ".//button[text()='Оформить заказ']"]
id_order = [By.XPATH, ".//p[text()='идентификатор заказа']/preceding-sibling::h2"]
modal_window = [
    By.XPATH, ".//p[contains(@class,'AppHeader_header__linkText__3q_va')]"]
