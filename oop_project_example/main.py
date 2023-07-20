from file_processors import JsonProcessor, CsvProcessor
from sku_logic import MetricCalculator

SOURCE_DIR = 'SKU'


if __name__ == '__main__':
    file_processors = [JsonProcessor(), CsvProcessor()]

    print('=' * 50 + '\nReading the data\n' + '=' * 50)
    overall_data = list()
    for fp in file_processors:
        fp.process_directory(SOURCE_DIR)
        print(f'{type(fp).__name__} has processed {len(fp.processed_filenames)} files '
              f'and acquired {len(fp.data)} SKU event entries')
        print(f'  Files processed: {", ".join(fp.processed_filenames[:5])}...')
        print(f'  Data acquired: {fp.data[:5]}...')
        print('-' * 50)
        overall_data += fp.data

    print('=' * 50 + '\nCalculating metrics\n' + '=' * 50)
    metrics = MetricCalculator(overall_data)
    metrics.calculate_all_metrics()
