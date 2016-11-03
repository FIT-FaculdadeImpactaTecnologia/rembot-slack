import os
import sys
import firebase

reload(sys)
sys.setdefaultencoding('utf-8')

class CacheCreator(object):

    def __init__(self):
        os.chdir('/home/vinicius/rembot')
        self.file = open('contact/teachers_cache.txt', 'w')
        self.firebase_client = firebase.FirebaseApplication("https://rembot-68f41.firebaseio.com/", None)

    def create(self):
        self.file.write(self.parse_data())
        self.file.close()

    def parse_data(self):
        data = self.retrieve_data()
        cache = ""
        for name in data:
            cache += "{}\n".format(name).lower()
        return cache

    def retrieve_data(self):
        return self.firebase_client.get("teachers_email", None)