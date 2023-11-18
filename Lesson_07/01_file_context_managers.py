filename = "name.txt"

with open(filename) as file:
    lines = file.readlines()
    # for line in file:
    #     print(line)


class FileBase:
    def __init__(self, filename: str) -> None:
        self.file = filename

    def close(self):
        print(f"Closing the {self.filename}")


class FileReader(FileBase):
    def readlines(self):
        print("Reading all lines from the file.")

    def writelines(self):
        print("Only for reading.")


class FileWriter(FileBase):
    def readlines(self):
        print("Only for writing.")

    def writelines(self, data: str):
        print("Writing the {data}")


# in construction with open, "open" -> class open


class open:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename: str = filename
        self.mode: str = mode

    # from __enter__ returns objects -> "as file:"

    def __enter__(self):
        if self.mode == "r":
            self.file_mode_instance = FileReader(self.filename)
        elif self.mode == "w":
            self.file_mode_instance = FileWriter(self.filename)
        else:
            raise NotImplementedError

        return self.file_mode_instance

    def __exit__(self, *args, **kwargs):
        self.file_mode_instance.close()
