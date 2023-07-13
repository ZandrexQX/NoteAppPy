class Note:
    def __init__(self, title, description):
        self.__title = title
        self.__description = description

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
    def get_note(self):
        return f"Название: {self.__title}\n" \
               f"Описание: {self.__description}\n"