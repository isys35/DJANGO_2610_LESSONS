from dataclasses import dataclass
import datetime


@dataclass
class Lesson:
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
            topics: list[Topic]
    ):
        self._lesson_duration = end_lesson.hour - start_lesson.hour
        self._first_lesson_date = first_lesson_date
        self._topics = topics
        self._lessons: list[Lesson] = []

    def execute(self):
        avialable_hours: int = self._lesson_duration
        lesson = None
        topic_names_for_lesson = []

        for topic in self._topics:
            if topic.hours <= avialable_hours:
                if not lesson:
                    lesson = Lesson()
                topic_names_for_lesson.append(topic.name)
                avialable_hours -= topic.hours
                if avialable_hours == 0:
                    avialable_hours = self._lesson_duration
                    lesson.name = " ".join(topic_names_for_lesson)
                    topic_names_for_lesson = []
                    self._lessons.append(lesson)
                    lesson = None
            else:
                topic_hours = topic.hours
                while topic_hours > avialable_hours:
                    topic_hours -= avialable_hours
                    if not lesson:
                        lesson = Lesson()
                    topic_names_for_lesson.append(topic.name)
                    avialable_hours = self._lesson_duration
                    lesson.name = " ".join(topic_names_for_lesson)
                    topic_names_for_lesson = []
                    self._lessons.append(lesson)
                    lesson = None
                else:
                    if not lesson:
                        lesson = Lesson()
                    topic_names_for_lesson.append(topic.name)
                    avialable_hours -= topic_hours
                    if avialable_hours == 0:
                        avialable_hours = self._lesson_duration
                        lesson.name = " ".join(topic_names_for_lesson)
                        topic_names_for_lesson = []
                        self._lessons.append(lesson)
                        lesson = None
        if lesson:
            lesson.name = " ".join(topic_names_for_lesson)
            self._lessons.append(lesson)
        return self._lessons


class LessonCreator:
    def __init__(self, create_lesson_service: CreateLessonsService):
        pass


if __name__ == "__main__":
    start_lesson = datetime.time(hour=17, minute=0)
    end_lesson = datetime.time(hour=20, minute=0)
    first_lesson_date = datetime.date(day=24, month=3, year=2023)
    topics = [Topic(name="Введение", hours=4), Topic(name="Типы данных", hours=1), Topic(name="Строки", hours=1)]
    CreateLessonsService(
        start_lesson,
        end_lesson,
        first_lesson_date,
        topics
    ).execute()
