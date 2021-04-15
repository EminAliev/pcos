class Question:

    def __init__(self, answers, text):
        self.answers = answers
        self.text = text

    def print_answers(self):
        for i in range(len(self.answers)):
            print('{0} - {1}'.format(i + 1, self.answers[i]))