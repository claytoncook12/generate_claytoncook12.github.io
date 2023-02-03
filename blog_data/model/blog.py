import typing as t
import datetime as datetime

class Blog:
    def __init__(
        self,
        title: str,
        date: str,
        short_desc: str,
        main_image: str,
        photo_credit: str,
        tags: t.List[str],
        html_file: str
    ):
        self.title = title
        self.date = date
        self.short_desc = short_desc
        self.main_image = main_image
        self.photo_credit = photo_credit
        self.tags = tags
        self.html_file = html_file