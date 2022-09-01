from customer import Customer
from soda_machine import SodaMachine
import user_interface

class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        
        soda_machine = SodaMachine()
        # soda_machine.fill_register() #this needs to be put somewhere(as opposed to not at all)
        # soda_machine.fill_inventory()#I added this herer
        will_proceed = False
        while will_proceed == False:# == False?
            user_option = user_interface.simulation_main_menu()
            if user_option == 1: #switched these into integers, it wont recognize these strings as it is converted earlier in the process
                soda_machine.begin_transaction(customer)
            elif user_option == 2:
                customer.check_coins_in_wallet()
            elif user_option == 3:
                customer.check_backpack()
            else:
                will_proceed = False
