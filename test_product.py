from product import product_details

def test_product_details():
    expected_output = (
        "Product Name   : Laptop\n"
        "Product ID     : F1007\n"
        "Quantity      : 1\n"
        "Price          : 95000"
    )
    assert product_details("Laptop", "F1007", 1, 95000) == expected_output
