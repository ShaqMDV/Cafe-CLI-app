import unittest # Imports the right framework we can use to create the unit test
from unittest.mock import patch # Allows the making of mock objects to be used in running the code. Replaces the actual object with the mock up.

from main_menu import main_menu
from products_menu import products_menu
from order_menu import orders_menu
from courier_menu import courier_menu


# Defining the class
class TestMainMenu(unittest.TestCase):
    def test_menu_functionality(self, menu_function, input_sequence):
        with patch('builtins.input', side_effect=input_sequence) as mock_input:
            menu_function()

            # Assert the correct number of calls
            self.assertEqual(len(input_sequence), mock_input.call_count)
        
        print(f"Test passed for menu_functionality with {menu_function.__name__} and input {input_sequence}")

    def test_products_menu(self):
        self.test_menu_functionality(products_menu, ["1", "0"])
        print("Test passed for products_menu")

    def test_orders_menu(self):
        self.test_menu_functionality(orders_menu, ["2", "0"])
        print("Test passed for orders_menu")

    def test_courier_menu(self):
        self.test_menu_functionality(courier_menu, ["3", "0"])
        print("Test passed for courier_menu")

    def test_exit_option(self):
        with patch('builtins.input', side_effect=["0"]), \
             patch('builtins.print') as mock_print:
            main_menu()

            mock_print.assert_any_call("\nData saved.\n")
            mock_print.assert_any_call("\nThanks for stopping by!\n")
        
        print("Test passed for exit_option")

    def test_invalid_option(self):
        with patch('builtins.input', side_effect=["invalid", "0"]), \
             patch('builtins.print') as mock_print:
            main_menu()

            mock_print.assert_any_call("Invalid choice, please try again :)\n")
        
        print("Test passed for invalid_option")
if __name__ == '__main__':
    unittest.main()