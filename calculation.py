#f = lambda *numbers: sum(numbers) / len(numbers)
'''def average(a, b):
    return (a + b)/2

def maximum(a, b):
    if a > b:
        return a
    else:
        return b
'''

email = 'USER4@DOMAIN.COM'.lower()
password = 'love'.lower()
users = [
    {"email": "user1@domain.com", "password": "password1"},
    {"email": "user2@domain.com", "password": "abcde"},
    {"email": "user3@domain.com", "password": "123456"},
    {"email": "user4@domain.com", "password": "lovelove"},
    {"email": "user5@domain.com", "password": "kdmUdmk84M"},
    {"email": "user7@domain.com", "password": "123456"},
    {"email": "user8@domain.com", "password": "123456"},
    {"email": "user9@mail.com.ru", "password": "password9"}
]
has_access = None

# Перебираем всех пользователей в цикле:
for user in users:
    if user["email"] == email:
        if user["password"] == password:
            has_access = True
        else:
            has_access = False

        break

# Выводим результат.
if has_access is None:
    print("Пользователь не найден")
elif has_access:
    print("Доступ открыт")
else:
    print("Доступ закрыт")


