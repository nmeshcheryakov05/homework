import datetime
import allure
now = datetime.datetime.now()


@allure.epic('G1')
@allure.feature('WEB и API')
@allure.story('Методы для работы со временем')
class WorkWithTime:

    @allure.step('Получение текущего времени компьютера')
    def get_date_time_for_sql_increased_x_days(self, timedelta_days=0):
        datetime2 = now + datetime.timedelta(days=timedelta_days)
        temp = datetime2.strftime("%Y-%m-%d %H:%M:%S")
        temp = temp + '.000'
        return temp
