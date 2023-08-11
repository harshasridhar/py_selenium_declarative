from enum import Enum


class Constants(str, Enum):
    # Actions
    ACTION_TYPE_GET = "get"
    ACTION_TYPE_CLICK = "click"
    ACTION_TYPE_TEXT = "text"
    ACTION_TYPE_SELECT = "select"
    ACTION_TYPE_SLEEP = "sleep"
    ACTION_TYPE_SCREENSHOT = "screenshot"
    AVAILABLE_ACTIONS = [
        ACTION_TYPE_GET,
        ACTION_TYPE_CLICK,
        ACTION_TYPE_TEXT,
        ACTION_TYPE_SELECT,
        ACTION_TYPE_SCREENSHOT,
        ACTION_TYPE_SLEEP,
    ]
