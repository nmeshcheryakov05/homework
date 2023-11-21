class GroupData:

    base_url = 'https://api-test-compose.gandiva.ru'
    base_url_web = 'https://web-test-compose.gandiva.ru'

    access_token = ''
    token_type = ''
    refresh_token = ''

    buttons_web = {
        'toWork': '//*[@class="ga_change_status"]/button',
        'assignToSelf': '//*[@class="ga_change_status"]/button',
        'toExamination': '//*[@id="to_resolved"]'
    }

    users_id_api = {
        'user1': {
            'id': '8166'
        },
        'user3': {
            'id': '8168'
        },
        'boss1': {
            'id': '179904'
        },
        'boss2': {
            'id': '179903'
        }
    }

    users_id = {
        'boss1': {
            'id': 'ap_179904'
        },
        'boss2': {
            'id': 'ap_179903'
        },
    }

    users = {
        'user1': {
            'log': 'user_8166@gandiva.ru',
            'pass': 'Qwerty1!',
        },
        'user2': {
            'log': 'gandiva_test_user2@mail.ru',
            'pass': 'Qwerty1!',
        },
        'user3': {
            'log': 'user_8168@gandiva.ru',
            'pass': 'Qwerty1!',
        },
        'user4': {
            'log': 'gandiva_test_user4@mail.ru',
            'pass': 'Qwerty1!',
        },
        'user5': {
            'log': 'gandiva_test_user5@mail.ru',
            'pass': 'Qwerty1!',
        },
        'boss1': {
            'log': 'user_179904@gandiva.ru',
            'pass': 'Qwerty1!',
        },
        'boss2': {
            'log': 'user_179903@gandiva.ru',
            'pass': 'Qwerty1!',
        },
        'boss3': {
            'log': 'gandiva_test_boss03@mail.ru',
            'pass': 'Qwerty1!',
        },
    }
