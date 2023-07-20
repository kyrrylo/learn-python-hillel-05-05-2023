from datetime import date, time, datetime


class SKUEventEntry:
    OPERATION_TYPES = {'first_arrival', 'sale', 'dispose', 'move'}

    def __init__(self, **kwargs):
        # self.<field_name>: <field_type> = <field_value>
        self.date: date = datetime.strptime(kwargs['date'], '%d-%b-%Y').date()
        self.time: time = datetime.strptime(kwargs['time'], '%H:%M:%S').time()
        self.sku: str = kwargs['sku']
        self.warehouse: str = kwargs['warehouse']
        self.warehouse_cell_id: int = int(kwargs['warehouse_cell_id'])

        if kwargs['operation'] in SKUEventEntry.OPERATION_TYPES:
            self.operation: str = kwargs['operation']
        else:
            raise ValueError(f'Unknown operation type: {kwargs["operation"]}')

        self.invoice: int = int(kwargs['invoice'])
        self.expiration_date: date = datetime.strptime(kwargs['expiration_date'], '%d-%b-%Y').date()
        self.operation_cost: float = float(kwargs['operation_cost'])
        self.comment: str = kwargs['comment']

    def expired(self) -> bool:
        """
        Compares SKU expiration date with today's date
        :return: True if expired, False if not
        """
        if datetime.today().date() > self.expiration_date:
            return True
        return False

    def __repr__(self):
        """
        Unlike __str__, __repr__ works when class objects are output inside lists too

        Although, it is best not to touch __repr__ as it is the main way to access variable address
        and as we define this method, we loose access to the address
        """
        return f'{self.operation.capitalize()} of {self.sku} at {self.date.strftime("%d-%b-%Y")}'
