from abc import ABC, abstractmethod
import sqlite3


class DataStorage(ABC):
    @abstractmethod
    def save(self, key, data):
        pass
    
    @abstractmethod
    def load(self, key):
        pass
    
    @abstractmethod
    def delete(self, key):
        pass

class FileStorage(DataStorage):
    def save(self, key, data):
        with open(key, 'w') as file:
            file.write(data)
    
    def load(self, key):
        with open(key, 'r') as file:
            return file.read()
    
    def delete(self, key):
        import os
        if os.path.exists(key):
            os.remove(key)

class DatabaseStorage(DataStorage):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.conn = None
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.connection_string)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()
    
    def save(self, key, data):
        with self.conn:
            self.conn.execute("INSERT INTO table_name (key, data) VALUES (?, ?)", (key, data))
    
    def load(self, key):
        with self.conn:
            result = self.conn.execute("SELECT data FROM table_name WHERE key = ?", (key,))
            return result.fetchone()[0] if result else None
    
    def delete(self, key):
        with self.conn:
            self.conn.execute("DELETE FROM table_name WHERE key = ?", (key,))

def test_storage(storage):
    storage.save('file.txt', 'This is some example data.')

    loaded_data = storage.load('file.txt')
    print("Loaded data:", loaded_data)

    storage.delete('file.txt')
    loaded_data_after_deletion = storage.load('file.txt')
    print("Data after deletion:", loaded_data_after_deletion)

if __name__ == "__main__":
    print("Testing FileStorage:")
    file_storage = FileStorage()
    test_storage(file_storage)

    print("\n")

    print("Testing DatabaseStorage:")
    db_storage = DatabaseStorage('your_connection_string')
    with db_storage:
        test_storage(db_storage)
