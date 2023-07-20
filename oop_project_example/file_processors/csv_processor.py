from .file_processor import FileProcessor
from sku_logic import SKUEventEntry
from os import listdir, path
import csv


class CsvProcessor(FileProcessor):
    def process_directory(self, dir_name: str):
        """
        Reads all *.csv files from dir_name and converts every line to SKUEventEntry class
        :param dir_name: name of the directory to process
        :return:
        """
        for file_name in listdir(dir_name):
            if file_name[-4:] != '.csv':
                continue
            full_file_name = path.join(dir_name, file_name)
            with open(full_file_name, newline='') as csv_fp:
                reader = csv.DictReader(csv_fp)
                for entry in reader:
                    # ** before dict converts it to **kwargs at the entrance
                    self.data.append(SKUEventEntry(**entry))
                self.processed_filenames.append(full_file_name)
