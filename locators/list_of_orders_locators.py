from selenium.webdriver.common.by import By

order_details = [By.XPATH, ".//div[contains(@class,'orderBox')]"]
order_card = [By.XPATH, "(.//a[contains(@href,'/feed/')])[2]"]
order_card_all = [By.XPATH, ".//a[contains(@href,'/feed/')]/div/p"]
order_card_in_orders_history = [
    By.XPATH, "(.//a[contains(@href,'/account/order-history/')])[1]/div/p[1]"]
order_card_in_orders_history_all = [
    By.XPATH, "(.//a[contains(@href,'/account/order-history/')])[1]/div/p[1]"]
order_list_header = [By.XPATH, ".//h1[text()='Лента заказов']"]
orders_completed_for_all_time = [
    By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p"]
orders_completed_for_today = [
    By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p"]
order_in_progress = [
    By.XPATH, ".//ul[contains(@class,'orderListReady')]/li"]
