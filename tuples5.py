# 5. 

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

def merge_catalogs(*catalogs):
    merged_catalog = ()
    for catalog in catalogs:
        merged_catalog += catalog
    return merged_catalog
merged_catalog = merge_catalogs(catalog1, catalog2)
print("Merged Catalog:")
for product in merged_catalog:
    print(product)
