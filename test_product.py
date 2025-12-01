from product import product_details

def test_product_details():
    expected_output = (
        "Product Name   : Laptop\n"
        "Product ID     : E1007\n"
        "Quantity      : \n1"
        "Price          : 95000"
    )
    assert product_details("Laptop", "E1007", 1, 95000) == expected_output
