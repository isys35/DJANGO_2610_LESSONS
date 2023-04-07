from courses import models
from roadmaps import models as rm_models
import datetime


class CreateLessonsService:

    def __init__(
            self,
            start_lesson: datetime.time,
            end_lesson: datetime.time,
            first_lesson_date: datetime.date,
            lesson_weekdays: list[int],
            topics: list[rm_models.Topic],
            course: models.Course
    ):
        self.start_lesson = start_lesson
        self.end_lesson = end_lesson
        self.lesson_duration = end_lesson.hour - start_lesson.hour
        self.first_lesson_date = first_lesson_date
        self.lesson_weekdays = lesson_weekdays
        self.topics = topics
        self.course = course

        self._lessons: list[models.CourseLesson] = []
        self._avialable_hours = self.lesson_duration
        self._lesson: models.CourseLesson | None = None
        self._topic_names_for_lesson: list[models.Topic] = []
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
            self._lesson = models.CourseLesson(
                started_at=self._get_lesson_datetime(),
                course_id=self.course.id
            )
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