from datetime import datetime

class Note:
    def __init__(self, title, description):
        self.instance_id = id(self)
        self.__title = title
        self.__description = description
        self.__date = datetime.now()

    def __str__(self):
        return self.__title

    def set_title(self, title):
        self.__title = title
    def get_title(self):
        return self.__title
    def set_description(self, decription):
        self.__description = decription
    def get_description(self):
        return self.__description
    def set_date(self, date):
        self.__date = date
    def get_date(self):
        return self.__date
    def get_note(self):
        return f"Название: {self.__title}\n" \
               f"Описание: {self.__description}\n" \
               f"Дата создания: {self.__date}\n"