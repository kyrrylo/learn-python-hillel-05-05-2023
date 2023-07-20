class FileProcessor:
    def __init__(self):
        self.processed_filenames = list()
        self.data = list()

    def process_directory(self, dir_name: str):
        """
        Implemented in subclasses
        Meant to add every processed file in self.processed_filenames and data from it in self.data
        :param dir_name: name of the directory to process
        """
        raise NotImplementedError
