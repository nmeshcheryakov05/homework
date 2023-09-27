import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestRequests:
    driver = None
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    def setup_method(self):
        self.driver.get('https://web-test-compose.gandiva.ru/Identity/Account/Login?ReturnUrl=%2F')
        time.sleep(1)

    def teardown_method(self):
        pass

    def test_requests(self):
        #ввод логина в поле
        self.driver.find_element(By.XPATH, '//*[@id="Input_UserName"]').send_keys('gandiva_test_user1@mail.ru')
        #ввод пароля в поле
        self.driver.find_element(By.XPATH, '//*[@id="Input_Password"]').send_keys('Qwerty1!')
        #клик по кнопке "Вход"
        self.driver.find_element(By.XPATH, '//*[@id="login-submit"]').click()
        time.sleep(2)

        #клик по кнопке "Заявки"
        self.driver.find_element(By.XPATH, '//*[@anchor="Requests"]').click()
        time.sleep(2)
        #клик по кнопке создания заявки для появления выпадающего списка
        self.driver.find_element(By.XPATH, '//*[@class="header__button"]').click()
        #клик по кнопке "Создать"
        self.driver.find_element(By.XPATH, '//*[@id="option-new"]').click()
        #клик по выбору отдела
        self.driver.find_element(By.XPATH, '//*[@id="Department_chosen"]').click()
        #вставка текста "Отдел тестирования Гандивы" в поле поиска, enter
        self.driver.find_element(By.XPATH, '//div[@id="Department_chosen"]//input[@class="chosen-search-field"]').send_keys('Отдел тестирования Гандивы', Keys.ENTER)
        #клик по выбору категории
        self.driver.find_element(By.XPATH, '//*[@id="Category_chosen"]').click()
        #вставка текста "Программное обеспечение", enter
        self.driver.find_element(By.XPATH, '//div[@id="Category_chosen"]//input[@class="chosen-search-field"]').send_keys('Программное обеспечение', Keys.ENTER)
        #клик по выбору типа
        self.driver.find_element(By.XPATH, '//*[@id="RequestType_chosen"]').click()
        #вставка текста "Тестовый", enter
        self.driver.find_element(By.XPATH, '//div[@id="RequestType_chosen"]//input[@class="chosen-search-field"]').send_keys('Тестовый', Keys.ENTER)
        #клик по выбору виду
        self.driver.find_element(By.XPATH, '//*[@id="JobType_chosen"]').click()
        #вставка текста "Тестовый", enter
        self.driver.find_element(By.XPATH, '//div[@id="JobType_chosen"]//input[@class="chosen-search-field"]').send_keys('Тестовый', Keys.ENTER)

        #присвоение переменной элемент iframe
        frame = self.driver.find_element(By.XPATH, '//*[@id="cke_1_contents"]/iframe')
        #переключение на другой фрейм
        self.driver.switch_to.frame(frame)

        #отправка текста "test" в поле ввода описания
        self.driver.find_element(By.XPATH, '//*[@class="cke_editable cke_editable_themed cke_contents_ltr"]').send_keys('test')

        #переключение на исходную страницу
        self.driver.switch_to.default_content()
        #клик по кнопке "Сохранить"
        self.driver.find_element(By.XPATH, '//*[@id="is3"]').click()
        time.sleep(1)
        #присвоение переменной request номера заявки
        request = self.driver.find_element(By.XPATH, '//*[@id="is11"]/div[1]/div[1]/b').text
        #усечение полученного текста для обрезки "№ "
        request = request[2:]

        #клик по кнопке пользователя
        self.driver.find_element(By.XPATH, '//*[@anchor="profile"]').click()
        #клик по кнопке "Выйти"
        self.driver.find_element(By.XPATH, '//*[@anchor="exit_user"]').click()
        #ввод логина в поле
        self.driver.find_element(By.XPATH, '//*[@id="Input_UserName"]').send_keys('gandiva_test_boss_1@mail.ru')
        #ввод пароля в поле
        self.driver.find_element(By.XPATH, '//*[@id="Input_Password"]').send_keys('Qwerty1!')
        #клик по кнопке "Вход"
        self.driver.find_element(By.XPATH, '//*[@id="login-submit"]').click()

        #прямой переход по ссылке на заявку, номер которой записан в переменной request
        self.driver.get(f'https://web-test-compose.gandiva.ru/Request/Edit/{request}')
        time.sleep(1)
        #клик по кнопке "Назначить на себя"
        self.driver.find_element(By.XPATH, '//*[@class="ga_bttn_status bttn_e"]').click()
        time.sleep(1)
        #клик по кнопке "Сохранить"
        self.driver.find_element(By.XPATH, '//*[@id="ga_save_btn"]').click()
        time.sleep(3)

        #проверяем, что заявка назначена на текущего пользователя
        assert self.driver.find_element(By.XPATH, '//*[@class="ga_user_inline ga_contractor last"]//*[@class="ga_user_name"]').text == 'Boss1 Test'