from enum import Enum

class SomePageLocators(str, Enum):
    POP_UP_TERMS = "div[data-qa='Card'] div[class*='Text_module_size14']"
    CALENDAR_DAY = "div[class*='CalendarDay_calendar-day'] div"
    DATE_INPUT = "div[class*='FormFields_secondary-input-white-date'] div[data-qa='TextInput']"