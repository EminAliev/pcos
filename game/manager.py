class Manager:
    reputation = 50
    quality = 0
    time = 100
    budget = 100

    def __str__(self):
        return 'Репутация: ' + str(self.reputation) + 'Качество: ' + str(self.quality) + 'Время: ' + str(
            self.time) + 'Бюджет: ' + str(self.budget)

    def point_results(self, quality, budget, reputation, time):
        self.reputation += reputation
        self.quality += quality
        self.time += time
        self.budget += budget
