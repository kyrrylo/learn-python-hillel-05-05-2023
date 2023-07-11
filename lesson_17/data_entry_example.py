source_data = list()

unique_sku = set()
for entry in source_data:
    unique_sku.add(entry.sku)
print(unique_sku)
