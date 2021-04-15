from random import randint

from game.manager import Manager
from game.question import Question


def random_luck(manager_reputation):
    digit = randint(0, 100)

    return digit <= manager_reputation


question_1 = Question(
    [
        'Буду распределять таски между сотрудниками',
        'Распределю таски в последний месяц',
    ],
    'Заказчик поставил дедлайн по проекту 3 месяца, ваши действия',
)

question_2 = Question(
    [
        'Объяснить, что изменения не нужны',
        'Дослушать и исправлять',
        'Начать проект заново',
    ],
    'Прошло 2 месяца и заказчик хочет все поменять в проекте, ваши действия',
)

question_3 = Question(
    [
        'Попросить у заказчика еще немного',
        'Отправить несколько сотрудников на увольнение',
        'Найти нового заказчика с новым проектом',
    ],
    'Заканчивается бюджет проекта, ваши действия',
)

question_4 = Question(
    [
        'Всех сотрудников на новый проект',
        'Половину сотрудников',
        'Откажусь от второго проекта',
    ],
    'Приходит второй заказчик с своим проектом, первый проект важный для репутации компании, другой - прибыльный. Как распределить таски?',
)

question_5 = Question(
    [
        'Сотрудники сами решат свои проблемы',
        'Найти новый состав команды',
        'Помочь сотрудникам',
    ],
    'Между сотрудниками возникла конфликтная ситуация, ваши действия',
)

manager = Manager()

print(question_1.text)
print(question_1.print_answers())
answer = int(input())
random_fl = random_luck(manager.reputation)
if answer == 1:
    manager.point_results(
        70 if random_fl else 30,
        -50 if random_fl else -80,
        0,
        -30 if random_fl else -50,
    )
elif answer == 2:
    manager.point_results(
        50 if random_fl else 30,
        -80,
        -20,
        -60 if random_fl else -120,
    )

print(question_2.text)
print(question_2.print_answers())
answer = int(input())
random_fl = random_luck(manager.reputation)

if answer == 1:
    manager.point_results(
        40 if random_fl else -20,
        0,
        -10,
        0,
    )
elif answer == 2:
    manager.point_results(
        40 if random_fl else -10,
        0,
        10,
        -10,
    )
elif answer == 3:
    manager.point_results(
        -30 if random_fl else -70,
        -50,
        0,
        -30 if random_fl else -50,
    )

print(question_3.text)
print(question_3.print_answers())
answer = int(input())
random_fl = random_luck(manager.reputation)

if answer == 1:
    manager.point_results(
        30 if random_fl else 0,
        30 if random_fl else 0,
        0 if random_fl else -10,
        0,
    )
elif answer == 2:
    manager.point_results(
        -10,
        0,
        -10,
        -10,
    )
elif answer == 3:
    manager.point_results(
        -5 if random_fl else -10,
        30,
        0,
        -5 if random_fl else -10,
    )

if answer == 3:

    print(question_4.text)
    print(question_4.print_answers())
    answer = int(input())
    random_fl = random_luck(manager.reputation)

    if answer == 1:
        manager.point_results(
            -20 if random_fl else -70,
            100,
            -10,
            40,
        )
    elif answer == 2:
        manager.point_results(
            -20 if random_fl else -40,
            70,
            5,
            -20,
        )
    elif answer == 3:
        manager.point_results(
            30 if random_fl else 0,
            0,
            0,
            40,
        )

print(question_5.text)
print(question_5.print_answers())
answer = int(input())
random_fl = random_luck(manager.reputation)

if answer == 1:
    manager.point_results(
        0 if random_fl else -20,
        0 if random_fl else -20,
        0 if random_fl else -10,
        0 if random_fl else -15,
    )
elif answer == 2:
    manager.point_results(
        10 if random_fl else -10,
        0 if random_fl else -10,
        0,
        10 if random_fl else -10,
    )
elif answer == 3:
    manager.point_results(
        10 if random_fl else -10,
        0,
        10 if random_fl else -10,
        10 if random_fl else -10,
    )

print(manager)

if manager.quality >= 75 and manager.time > 0 and manager.reputation > 0 and manager.budget > 0:
    print('Вы настоящий PM!')
else:
    print('Пройдите снова')
