class Course:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def _get_name(self):
        return self.__name

    def _get_id(self):
        return self.__id

    def display(self):
        print(f"Course name: {self.__name}, Course ID: {self.__id}")