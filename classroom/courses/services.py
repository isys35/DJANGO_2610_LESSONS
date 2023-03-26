from dataclasses import dataclass
import datetime


@dataclass
class Lesson:
    started_at: datetime.datetime
    name: str = ""


@dataclass
class Topic:
    name: str
    hours: int


class CreateLessonsService:

    def __init__(
            self,
            start_lesson: datetime.time,
            end_lesson: datetime.time,
            first_lesson_date: datetime.date,
            lesson_weekdays: list[int],
            topics: list[Topic]
    ):
        self.start_lesson = start_lesson
        self.end_lesson = end_lesson
        self.lesson_duration = end_lesson.hour - start_lesson.hour
        self.first_lesson_date = first_lesson_date
        self.lesson_weekdays = lesson_weekdays
        self.topics = topics

        self._lessons: list[Lesson] = []
        self._avialable_hours = self.lesson_duration
        self._lesson: Lesson | None = None
        self._topic_names_for_lesson: list[Topic] = []
        self._lesson_started_at: datetime.datetime | None = None

    def execute(self):
        return self.create_lessons()

    def _get_lesson_datetime(self):
        if not self._lesson_started_at:
            self._lesson_started_at = datetime.datetime(
                day=self.first_lesson_date.day,
                month=self.first_lesson_date.month,
                year=self.first_lesson_date.year,
                hour=self.start_lesson.hour
            )
            return self._lesson_started_at
        while True:
            self._lesson_started_at += datetime.timedelta(days=1)
            if self._lesson_started_at.weekday() in self.lesson_weekdays:
                return self._lesson_started_at

    def _get_lesson(self):
        if not self._lesson:
            self._lesson = Lesson(started_at=self._get_lesson_datetime())
        return self._lesson

    def _append_lesson(self, lesson):
        self._avialable_hours = self.lesson_duration
        lesson.name = " ".join(self._topic_names_for_lesson)
        self._topic_names_for_lesson = []
        self._lessons.append(lesson)
        self._lesson = None

    def _action_small_topic(self, topic, fewer_hours):
        lesson = self._get_lesson()
        self._topic_names_for_lesson.append(topic.name)
        self._avialable_hours -= fewer_hours
        if self._avialable_hours == 0:
            self._append_lesson(lesson)

    def _action_big_topic(self, topic):
        topic_hours = topic.hours
        while topic_hours > self._avialable_hours:
            topic_hours -= self._avialable_hours
            lesson = self._get_lesson()
            self._topic_names_for_lesson.append(topic.name)
            self._append_lesson(lesson)
        else:
            self._action_small_topic(topic, topic_hours)

    def create_lessons(self):
        for topic in self.topics:
            if topic.hours <= self._avialable_hours:
                self._action_small_topic(topic, topic.hours)
            else:
                self._action_big_topic(topic)
        if self._lesson:
            self._append_lesson(self._lesson)
        return self._lessons


if __name__ == "__main__":
    start_lesson = datetime.time(hour=17, minute=0)
    end_lesson = datetime.time(hour=20, minute=0)
    lesson_weekdays = [2, 4]
    first_lesson_date = datetime.date(day=24, month=3, year=2023)
    topics = [Topic(name="Введение", hours=4), Topic(name="Типы данных", hours=7), Topic(name="Строки", hours=1)]
    print(CreateLessonsService(
        start_lesson,
        end_lesson,
        first_lesson_date,
        lesson_weekdays,
        topics
    ).execute())
