from enum import Enum

class SubjectEnum(str, Enum):
    MATH_PROF = "math_prof"
    RUSSIAN = "russian"
    PHYSICS = "physics"
    INF = "informatics"

SUBJECT_NAMES = {
    SubjectEnum.MATH_PROF: "Математика профиль",
    SubjectEnum.RUSSIAN: "Русский язык",
    SubjectEnum.PHYSICS: "Физика",
    SubjectEnum.INF: "Информатика",
}