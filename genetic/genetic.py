from random import randint

alphabet = "qwertyuiopasdfghjklzxcvbnm "

individuals_one = 51  # количество особей в 1 поколении.
individuals_crossing = 9  # количество особей, отбираемых для скрещивания
mutation = 82  # шанс мутациии


class Genetic():
    def __init__(self, text=None, len_text=0):
        if text:
            self.text = text
        else:
            self.text = "".join(alphabet[randint(0, len(alphabet) - 1)] for _ in range(len_text))

    def __len__(self):
        return len(self.text)

    def __getitem__(self, val):
        print(val)

    def genetic_check(self):
        '''
        Количество схожих символов в текущем гене и гене, который нужно получить.
        :return: s
        '''
        s = 0
        for i in range(len(self.text)):
            if self.text[i] != input.text[i]:
                s += 1
        return s

    def genetic_mutations(self):
        '''
        Заменяет случайный символ в гене на случайный символ из алфавита.
        :return:
        '''
        number = randint(0, len(self.text) - 1)
        s = list(self.text)
        s[number] = alphabet[randint(0, len(alphabet) - 1)]
        self.text = ''.join(s)


def genetic_selection(t1, t2):
    """
    Скрещивание двух генов
    :param t1: первый ген
    :param t2: второй ген
    :return: new_genetic
    """
    number = randint(1, len(t1) // 2)
    text = ""
    for i in range(len(t1)):
        if i % 2:
            text += t1.text[i * number: i * number + number]
        else:
            text += t2.text[i * number: i * number + number]
    new_genetic = Genetic(text, len(t1))
    if randint(0, 100) <= mutation:
        new_genetic.genetic_mutations()
    return new_genetic


def check_result(list_gen, search):
    '''
    Проверка на получение нужного гена
    :param list_gen: список генов
    :param search: поиск по генам
    :return: result
    '''
    result = True
    for i in list_gen:
        if i.text == search.text:
            result = False
            break
    return result


def main():
    global population
    while check_result(population, input):
        print(population[len(population) - 1].text)
        population = sorted(population, key=lambda x: x.genetic_check())[0:individuals_crossing]
        s = []
        for i in range(len(population)):
            for j in range(i + 1, len(population)):
                s.append(genetic_selection(population[i], population[j]))
        population = s
    print(input.text)


if __name__ == '__main__':
    print('Введите имя: ')
    name = input()
    input = Genetic(name, len(name))
    population = [Genetic(len_text=len(name)) for _ in range(individuals_one)]
    main()
