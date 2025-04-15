class Talk:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = start_time  # формат "HH:MM"
        self.duration = duration  # в минутах

    def end_time(self):
        hours, minutes = map(int, self.start_time.split(':'))
        minutes += self.duration
        hours += minutes // 60
        minutes %= 60
        return f"{hours:02}:{minutes:02}"

class Conference:
    def __init__(self):
        self.talks = []

    def add_talk(self, talk):
        for existing_talk in self.talks:
            if (talk.start_time < existing_talk.end_time() and
                existing_talk.start_time < talk.end_time()):
                print("Ошибка: Перекрытие во времени.")
                return
        self.talks.append(talk)
        print(f"Добавлено выступление: {talk.topic}")

    def total_duration(self):
        return sum(talk.duration for talk in self.talks)

    def longest_break(self):
        if not self.talks:
            return 0
        breaks = []
        sorted_talks = sorted(self.talks, key=lambda t: t.start_time)
        for i in range(1, len(sorted_talks)):
            start_prev = sorted_talks[i-1].end_time()
            start_curr = sorted_talks[i].start_time
            breaks.append((int(start_curr.split(':')[0]) * 60 + int(start_curr.split(':')[1])) -
                           (int(start_prev.split(':')[0]) * 60 + int(start_prev.split(':')[1])))
        return max(breaks)

# Пример использования
conference = Conference()
while True:
    topic = input("Введите тему доклада (или 'выход' для завершения): ")
    if topic.lower() == 'выход':
        break
    start_time = input("Введите время начала доклада (HH:MM): ")
    duration = int(input("Введите длительность доклада (в минутах): "))
    talk = Talk(topic, start_time, duration)
    conference.add_talk(talk)

print(f"Общее время докладов: {conference.total_duration()} минут.")
print(f"Самый длинный перерыв: {conference.longest_break()} минут.")
