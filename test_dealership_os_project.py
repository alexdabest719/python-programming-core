import os
import csv
import pytest
from dealership_os_project import calculate_financing, parse_vendor_string, export_inventory, Car

def test_calculate_financing():
    assert calculate_financing(25000, 5000, 60, 5.0) == 377.42
    assert calculate_financing(20000, 0, 60, 0) == 333.33

def test_parse_vendor_string():
    raw_string = "   Toyota ,  Camry  , 25000 , 4 "
    
    expected_output = {
        "Make": "Toyota",
        "Model": "Camry",
        "Price": 25000.0,
        "Doors": 4
    }
    
    assert parse_vendor_string(raw_string) == expected_output

def test_export_inventory():
    test_inventory = [Car("Honda", "Civic", 22000, 4)]
    test_filename = "test_inventory.csv"
    
    assert export_inventory(test_inventory, test_filename) == True
    assert os.path.exists(test_filename)
    
    with open(test_filename, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        assert rows[0]["Make"] == "Honda"
        assert rows[0]["Price"] == "22000.0" 
        
    os.remove(test_filename)