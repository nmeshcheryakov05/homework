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
        self.driver.find_element(By.XPATH, '//*[@id="Input_UserName"]').send_keys('gandiva_test_user1@mail.ru')
        self.driver.find_element(By.XPATH, '//*[@id="Input_Password"]').send_keys('Qwerty1!')
        self.driver.find_element(By.XPATH, '//*[@id="login-submit"]').click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//*[@anchor="Requests"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="header__button"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="option-new"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="Department_chosen"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="Department_chosen"]//input[@class="chosen-search-field"]').send_keys('Отдел тестирования Гандивы', Keys.ENTER)
        self.driver.find_element(By.XPATH, '//*[@id="Category_chosen"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="Category_chosen"]//input[@class="chosen-search-field"]').send_keys('Программное обеспечение', Keys.ENTER)
        self.driver.find_element(By.XPATH, '//*[@id="RequestType_chosen"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="RequestType_chosen"]//input[@class="chosen-search-field"]').send_keys('Тестовый', Keys.ENTER)
        self.driver.find_element(By.XPATH, '//*[@id="JobType_chosen"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="JobType_chosen"]//input[@class="chosen-search-field"]').send_keys('Тестовый', Keys.ENTER)

        frame = self.driver.find_element(By.XPATH, '//*[@id="cke_1_contents"]/iframe')
        self.driver.switch_to.frame(frame)

        self.driver.find_element(By.XPATH, '//*[@class="cke_editable cke_editable_themed cke_contents_ltr"]').send_keys('test')

        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, '//*[@id="is3"]').click()
        time.sleep(1)
        request = self.driver.find_element(By.XPATH, '//*[@id="is11"]/div[1]/div[1]/b').text
        request = request[2:]

        self.driver.find_element(By.XPATH, '//*[@anchor="profile"]').click()
        self.driver.find_element(By.XPATH, '//*[@anchor="exit_user"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="Input_UserName"]').send_keys('gandiva_test_boss_1@mail.ru')
        self.driver.find_element(By.XPATH, '//*[@id="Input_Password"]').send_keys('Qwerty1!')
        self.driver.find_element(By.XPATH, '//*[@id="login-submit"]').click()

        self.driver.get(f'https://web-test-compose.gandiva.ru/Request/Edit/{request}')
        self.driver.find_element(By.XPATH, '//*[@class="ga_bttn_status bttn_e"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="ga_save_btn"]').click()
        time.sleep(3)

        assert self.driver.find_element(By.XPATH, '//*[@class="ga_user_inline ga_contractor last"]//*[@class="ga_user_name"]').text == 'Boss1 Test'