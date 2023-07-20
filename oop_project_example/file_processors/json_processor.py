from .file_processor import FileProcessor
from sku_logic import SKUEventEntry
from os import listdir, path
import json


class JsonProcessor(FileProcessor):
    def process_directory(self, dir_name: str):
        for file_name in listdir(dir_name):
            if file_name[-5:] != '.json':
                continue
            full_file_name = path.join(dir_name, file_name)
            entries = json.load(open(full_file_name))
            entries = entries['data']
            for entry in entries:
                # ** before dict converts it to **kwargs at the entrance
                self.data.append(SKUEventEntry(**entry))
            self.processed_filenames.append(full_file_name)