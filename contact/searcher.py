import os
import firebase

class Searcher(object):

    def __init__(self, pattern):
        path = '{}/teachers_cache.txt'.format(os.getcwd())
        self.pattern = pattern
        self.teachers_file = open(path, 'r')
        self.firebase_client = firebase.FirebaseApplication("https://rembot-68f41.firebaseio.com/", None)
        self.teacher_info = dict()

    def search(self):
        teachers_list = self.search_for_pattern()
        print teachers_list
        if not len(teachers_list) == 0:
            string = ""
            for teacher in teachers_list:
                email = self.parse_info(teacher)
                string += "professor: {}\nemail: {}".format(teacher, email)
            return string
        else:
            return 'Nenhum professor encontrado :exclamation:'

    def parse_info(self, teacher_name):
        return self.firebase_client.get("/teachers_email", teacher_name)

    def search_for_pattern(self):
        teacher_list = []
        for line in self.teachers_file:
            if self.pattern in line:
                teacher_list.append(line.replace('\n', ''))
        return teacher_list