class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, position):
        del self.entries[position]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     with open(filename, 'w') as file:
    #         file.write(str(self))

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as file:
            file.write(str(journal))

    @staticmethod
    def load_from_file(journal, filename):
        pass

    @staticmethod
    def load_from_web(uri):
        pass

j = Journal()
j.add_entry('i cried today')
j.add_entry('i ate a bug')
j.add_entry('i had an interview today')
j.add_entry('fridge sales')

filename = "./.data/app.txt"
PersistenceManager.save_to_file(j, filename)

with open(filename) as fh:
    print(fh.read())