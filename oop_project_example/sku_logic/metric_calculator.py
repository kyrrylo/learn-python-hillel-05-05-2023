from typing import List
from .event_entry import SKUEventEntry
from os import path, makedirs


class MetricCalculator:
    RESULTS_DIR = 'results'

    # when specifying type of elements in list/tuple/dict, you can use typing library:
    # List[<data_type>] or Dict[<key_data_type>, <value_data_type>] or Tuple[<data_type>]
    def __init__(self, data: List[SKUEventEntry]):
        self.data = data

        makedirs(self.RESULTS_DIR, exist_ok=True)

        self.sku_index = self.create_sku_index(self.data)
        # create index is a better method as it unites all 3, but more difficult to construct
        # self.sku_index = self.create_index(self.data, 'sku')

        self.warehouse_index = self.create_warehouse_index(self.data)
        # create index is a better method as it unites all 3, but more difficult to construct
        # self.warehouse_index = self.create_index(self.data, 'warehouse')

        self.operation_index = self.create_operation_index(self.data)
        # create index is a better method as it unites all 3, but more difficult to construct
        # self.operation_index = self.create_index(self.data, 'operation')

    def create_warehouse_index(self, data: list, data_is_indexed=False) -> dict:
        index = dict()
        for i, entry in enumerate(data):
            if data_is_indexed:
                entry = self.data[entry]
            value = entry.warehouse
            if value not in index:
                index[value] = list()
            index[value].append(i)
        return index

    def create_sku_index(self, data: list, data_is_indexed=False) -> dict:
        index = dict()
        for i, entry in enumerate(data):
            if data_is_indexed:
                entry = self.data[entry]
            value = entry.sku
            if value not in index:
                index[value] = list()
            index[value].append(i)
        return index

    def create_operation_index(self, data: list, data_is_indexed=False) -> dict:
        index = dict()
        for i, entry in enumerate(data):
            if data_is_indexed:
                entry = self.data[entry]
            value = entry.operation
            if value not in index:
                index[value] = list()
            index[value].append(i)
        return index

    def create_index(self, data: list, field_name: str, data_is_indexed: bool = False) -> dict:
        index = dict()
        for i, entry in enumerate(data):
            if data_is_indexed:
                entry = self.data[entry]
            # getattr works like dict.get(), but made for classes
            # with this method you can access class fields through string
            value = getattr(entry, field_name)
            if value not in index:
                index[value] = list()
            index[value].append(i)
        return index

    def sale_income(self) -> float:
        """
        Calculates income from all sale operations
        :return: income value
        """
        income = float()
        for entry_id in self.operation_index['sale']:
            # indices return data in IDs
            income += self.data[entry_id].operation_cost
        return income

    def expired_sku(self, output_filename: str = None) -> list:
        """
        Finds which SKU expired before sale and had to be disposed or are yet to be disposed
        :param output_filename: if specified, writes response also into the file
        :return: list of expired and not sold SKUs
        """
        expired = list()
        for sku, entry_ids in self.sku_index.items():
            # indices return data in IDs
            last_entry = self.data[entry_ids[-1]]
            # working on SKUs which don't have sale as their last operation
            # and choosing those that expired
            if last_entry.operation != 'sale' and last_entry.expired():
                expired.append(last_entry.sku)
        if output_filename:
            with open(output_filename, 'w') as f:
                f.write('\n'.join(expired))
        return expired

    def warehouse_distribution(self, output_filename: str = None) -> dict:
        """
        Calculates how many SKUs each warehouse had in the past
        :param output_filename: if specified, writes response also into the file
        :return: dict of warehouse -> sku count pairs
        """
        wh_distr = dict()
        for wh_id, entry_ids in self.warehouse_index.items():
            sku_index = self.create_sku_index(entry_ids, data_is_indexed=True)
            # create index is a better method as it unites all 3, but more difficult to construct
            # sku_index = self.create_index(entry_ids, 'sku', data_is_indexed=True)

            wh_distr[wh_id] = len(sku_index.keys())
        if output_filename:
            with open(output_filename, 'w') as f:
                f.write('warehouse,sku_count\n')
                for wh_id, sku_count in wh_distr.items():
                    f.write(f'{wh_id},{sku_count}\n')
        return wh_distr

    def operations_per_warehouse(self, operation_type: str, output_filename: str = None) -> dict:
        """
        Calculates how many operation types happened on each warehouse
        :param operation_type: type of operation to calculate
        :param output_filename: if specified, writes response also into the file
        :return: warehouses sell distribution
        """
        op_distro = dict()
        # making sure all warehouses will be listed
        for warehouse in self.warehouse_index:
            op_distro[warehouse] = 0
        # calculating operation types
        for entry_id in self.operation_index[operation_type]:
            entry = self.data[entry_id]
            op_distro[entry.warehouse] += 1
        if output_filename:
            with open(output_filename, 'w') as f:
                f.write('warehouse,count\n')
                for wh_id, count in op_distro.items():
                    f.write(f'{wh_id},{count}\n')
        return op_distro

    def calculate_all_metrics(self):
        """
        This method collects all metrics and outputs them in a readable way
        """
        print(f'Calculating income from all sales...')
        income = self.sale_income()
        print(f'Income: {income:.2f} UAH')
        print('-' * 50)

        print(f'Fetching expired and not sold SKUs...')
        output_filename = path.join(self.RESULTS_DIR, 'expired_sku.txt')
        expired_sku = self.expired_sku(output_filename=output_filename)
        print(f'Expired not sold SKUs: {len(expired_sku)}')
        print(f'  {", ".join(expired_sku[:10])}...')
        print(f'Full listing available at {output_filename}')
        print('-' * 50)

        print(f'Fetching how many SKUs went through each warehouse...')
        output_filename = path.join(self.RESULTS_DIR, 'warehouse_load_distribution.csv')
        warehouse_distro = self.warehouse_distribution(output_filename=output_filename)
        for key, value in warehouse_distro.items():
            print(f'  Warehouse {key}: {value} SKUs')
        print(f'Listing available at {output_filename}')
        print('-' * 50)

        print(f'Fetching how many SKU sales were done through each warehouse...')
        output_filename = path.join(self.RESULTS_DIR, 'warehouse_sales.csv')
        warehouse_distro = self.operations_per_warehouse('sale', output_filename=output_filename)
        for key, value in warehouse_distro.items():
            print(f'  Warehouse {key}: {value} sales')
        print(f'Listing available at {output_filename}')
        print('-' * 50)

        print(f'Fetching how many SKU disposals were done at each warehouse...')
        output_filename = path.join(self.RESULTS_DIR, 'warehouse_disposals.csv')
        warehouse_distro = self.operations_per_warehouse('dispose', output_filename=output_filename)
        for key, value in warehouse_distro.items():
            print(f'  Warehouse {key}: {value} disposals')
        print(f'Listing available at {output_filename}')
        print('=' * 50)
