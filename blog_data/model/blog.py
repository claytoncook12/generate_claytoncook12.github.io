import re
import typing as t
import datetime as datetime

def slugify(s: str) -> str:
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$#.', '', s)
  return s

class Tag:
    def __init__(
            self,
            tag: str
    ):
        self.tag = tag

    def __str__(self) -> str:
        return self.tag
    
    def tag_slug(self) -> str:
        return slugify(self.tag)

class Blog:
    def __init__(
        self,
        title: str,
        date: str,
        short_desc: str,
        main_image: str,
        photo_credit: str,
        tags: t.List[Tag],
        html_file: str
    ):
        self.title = title
        self.date = date
        self.short_desc = short_desc
        self.main_image = main_image
        self.photo_credit = photo_credit
        self.tags = [Tag(tag) for tag in tags]
        self.html_file = html_file