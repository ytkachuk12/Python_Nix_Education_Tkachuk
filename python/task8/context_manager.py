"""
Context file manager. (similar to built-in func "with")
This manager provides data protection.
The file will be recorded only in case of complete recording all data
Otherwise we will roll back to previous state of file
"""
import os


class FileManager:
    """file manger"""
    def __init__(self, filename: str, mode="w"):
        self.filename = filename
        self.mode = mode
        self.temp_file = "temp.txt"

    def __enter__(self):
        self.file = open(self.temp_file, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_message, traceback):
        self.file.close()
        # check if wrote data was successful rename our temp.txt file to proper .txt file
        if exc_type is None:
            os.rename(self.file.name, self.filename)
        else:
            # else delete temp.txt file
            os.unlink(self.file.name)


if __name__ == "__main__":
    items = [
        "hi", "if only half data will be write in file!",\
        "you will lose nothing!", "all your previous data will be safe"
            ]

    with FileManager("data.txt", "w") as file:
        for count, item in enumerate(items):
            file.write(f"{item}\n")
            # last line just for checking
            # raise Exception("no wrote")
