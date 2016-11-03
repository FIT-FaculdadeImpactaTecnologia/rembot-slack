from contactsearcher import ContactSearcher
from cachecreator import CacheCreator
from searcher import Searcher

def main():
    # Save contact table in firebase
    searcher = ContactSearcher()
    searcher.execute()

    # Create teachers cache
    cache = CacheCreator()
    cache.create()

    # teacher_searcher = Searcher("vicente")
    # print teacher_searcher.search()

if __name__ == '__main__':
    main()