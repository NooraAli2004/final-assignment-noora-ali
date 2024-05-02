import tkinter as tk  # Importing the tkinter module
from tkinter import messagebox, simpledialog  #Importing specific modules from tkinter
import pickle #imported the pickle module

class Employee:  #Defining a class named Employee
    def __init__(self, name, emp_id, department, job_title, basic_salary, manager_id=None):  # Initializing the Employee class with attributes
        self.name = name  # Assigning the 'name' attribute
        self.emp_id = emp_id  # Assigning the 'emp_id' attribute
        self.department = department  # Assigning the 'department' attribute
        self.job_title = job_title  # Assigning the 'job_title' attribute
        self.basic_salary = basic_salary  # Assigning the 'basic_salary' attribute
        self.manager_id = manager_id  # Assigning the 'manager_id' attribute with a default value of None

class Client:  # Defining a class named Client
    def __init__(self, name, client_id, address, contact, budget):  # Initializing the Client class with attributes
        self.name = name  # Assigning the 'name' attribute
        self.client_id = client_id  # Assigning the 'client_id' attribute
        self.address = address  # Assigning the 'address' attribute
        self.contact = contact  # Assigning the 'contact' attribute
        self.budget = budget  # Assigning the 'budget' attribute

class Guest:  # Defining a class named Guest
    def __init__(self, name, guest_id):  # Initializing the Guest class with attributes
        self.name = name  # Assigning the 'name' attribute
        self.guest_id = guest_id  # Assigning the 'guest_id' attribute

class Event:  # Defining a class named Event
    def __init__(self, event_id, clients=None, guests=None):  # Initializing the Event class with attributes
        self.event_id = event_id  # Assigning the 'event_id' attribute
        self.clients = clients if clients else []  #Assigning the 'clients' attribute with an empty list if not provided
        self.guests = guests if guests else []  # Assigning the 'guests' attribute with an empty list if not provided

    def add_client(self, client):  # defining a method to add a client to the event
        self.clients.append(client)  # appending the client to the 'clients' list

    def add_guest(self, guest):  # defining a method to add a guest to the event
        self.guests.append(guest)  # Appending the guest to the 'guests' list

    def save_object(obj, filename): # Function to save an object to a binary file
        with open(filename, 'wb') as file:  # Opening a file in write-binary mode
            pickle.dump(obj, file)  # Serializing the object and writing it to the file

    def load_object(filename):  # Function to load an object from a binary file
        with open(filename, 'rb') as file:  # Opening a file in read-binary mode
            return pickle.load(file)  # Deserializing the object from the file and returning it

# Creating Employees
susan_meyers = Employee("Susan Meyers", 47899, "Sales", "Manager", 37500)  # Creating an instance of Employee
joy_rogers = Employee("Joy Rogers", 81774, "Sales", "Manager", 24000)  # Creating an instance of Employee
shyam_sundar = Employee("Shyam Sundar", 11234, "Sales", "Salesperson", 20000, manager_id=47899)  # Creating an instance of Employee with a specified manager_id
mariam_khalid = Employee("Mariam Khalid", 98394, "Sales", "Salesperson", 20000, manager_id=81774)  # Creating an instance of Employee with a specified manager_id
salem_j_sam = Employee("Salem J Sam", 98637, "Sales", "Salesperson", 20000, manager_id=47899)  # Creating an instance of Employee with a specified manager_id

# Creating Clients
client1 = Client("Noora", 1, "Al Barsha", "055877689", 800)  # Creating an instance of Client
client2 = Client("Hessa", 2, "Al Salamah", "83033933", 500)  # Creating an instance of Client

# Creating Guests
guest1 = Guest("Ayesha", 1)
guest2 = Guest("Maryam", 2)
guest3 = Guest("Hessa", 3)
guest4 = Guest("Fatma", 4)

# Creating an Event and adding clients and guests
event1 = Event(1)  # Creating an instance of Event
event1.add_client(client1)  # Adding client1 to the event
event1.add_client(client2)  # Adding client2 to the event
event1.add_guest(guest1)  # Adding guest1 to the event
event1.add_guest(guest2)  # Adding guest2 to the event



class EventType:  # Defining a class named EventType
    def __init__(self, name):  # Initializing the EventType class with an attribute
        self.name = name  # Assigning the 'name' attribute

class Venue:  # Defining a class named Venue
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):  # Initializing the Venue class with attributes
        self.venue_id = venue_id  # Assigning the 'venue_id' attribute
        self.name = name  # Assigning the 'name' attribute
        self.address = address  # Assigning the 'address' attribute
        self.contact = contact  # Assigning the 'contact' attribute
        self.min_guests = min_guests  # Assigning the 'min_guests' attribute
        self.max_guests = max_guests  # Assigning the 'max_guests' attribute

class Supplier:  # Defining a class named Supplier
    def __init__(self, supplier_id, name, address, contact):  # Initializing the Supplier class with attributes
        self.supplier_id = supplier_id  # Assigning the 'supplier_id' attribute
        self.name = name  # Assigning the 'name' attribute
        self.address = address  # Assigning the 'address' attribute
        self.contact = contact  # Assigning the 'contact' attribute

class Caterer:  # Defining a class named Caterer
    def __init__(self, caterer_id, name, address, contact, menu, min_guests, max_guests):  # Initializing the Caterer class with attributes
        self.caterer_id = caterer_id  # Assigning the 'caterer_id' attribute
        self.name = name  # Assigning the 'name' attribute
        self.address = address  # Assigning the 'address' attribute
        self.contact = contact  # Assigning the 'contact' attribute
        self.menu = menu  # Assigning the 'menu' attribute
        self.min_guests = min_guests  # Assigning the 'min_guests' attribute
        self.max_guests = max_guests  # Assigning the 'max_guests' attribute

class Event:  # Defining a class named Event
    def __init__(self, event_id, event_type, theme, date, time, duration, venue, client, guests=None,
                 catering_company=None, cleaning_company=None, decorations_company=None,
                 entertainment_company=None, furniture_company=None, invoice=None):  # Initializing the Event class with attributes
        self.event_id = event_id  # Assigning the 'event_id' attribute
        self.event_type = event_type  # Assigning the 'event_type' attribute
        self.theme = theme  # Assigning the 'theme' attribute
        self.date = date  # Assigning the 'date' attribute
        self.time = time  # Assigning the 'time' attribute
        self.duration = duration  # Assigning the 'duration' attribute
        self.venue = venue  # Assigning the 'venue' attribute
        self.client = client  # Assigning the 'client' attribute
        self.guests = guests if guests else []  # using if statement to assign the 'guests' attribute and else statement is no guest is provided.
        self.catering_company = catering_company  # Assigning the 'catering_company' attribute
        self.cleaning_company = cleaning_company  # Assigning the 'cleaning_company' attribute
        self.decorations_company = decorations_company  # Assigning the 'decorations_company' attribute
        self.entertainment_company = entertainment_company  # Assigning the 'entertainment_company' attribute
        self.furniture_company = furniture_company  # Assigning the 'furniture_company' attribute
        self.invoice = invoice  # Assigning the 'invoice' attribute

    def add_guest(self, guest):  # defining a method to add a guest to the event
        self.guests.append(guest)  # Appending the guest to the 'guests' list

    def save_object(obj, filename):  # Function to save an object to a binary file
        with open(filename, 'wb') as file:  # Opening a file in write-binary mode
            pickle.dump(obj, file)  # Serializing the object and writing it to the file

    def load_object(filename):  # Function to load an object from a binary file
        with open(filename, 'rb') as file:  # Opening a file in read-binary mode
            return pickle.load(file)  # Deserializing the object from the file and returning it

# Creating EventType instances
wedding = EventType("Wedding")  # Creating an instance of EventType
birthday = EventType("Birthday")  # Creating an instance of EventType
themed_party = EventType("Themed Party")  # Creating an instance of EventType
graduation = EventType("Graduation")  # Creating an instance of EventType

# Creating Venue instances
venue1 = Venue(1, "Dubai venue", "Jumeriah", "08898278", 50, 200)
venue2 = Venue(2, "Sharjah venue", "AlQoaz", "92902920", 30, 100)

# Creating Supplier instances
catering_supplier = Supplier(1, "Catering Company", "Al sweihat", "04786837")
cleaning_supplier = Supplier(2, "Cleaning Company", "Al Barsha", "029742940")
decorations_supplier = Supplier(3, "Decorations Company", "Jumeirah", "74829749")
entertainment_supplier = Supplier(4, "Entertainment Company", "Jumeirah", "08987492")
furniture_supplier = Supplier(5, "Furniture Company", "Al Barsha", "067363839")

# Creating Caterer instances
caterer1 = Caterer(1, "Hafla", "Al sweihat", "0488878", "desserts and sweets", 50, 200)
caterer2 = Caterer(2, "Bouffage", "Ras Al Khor", "06928729", "Labanese food", 30, 100)

# Creating Event instances
event1 = Event(1, wedding, "Traditional Wedding", "2024-05-15", "18:00", "4 hours", venue1, client1,
               catering_company=catering_supplier, decorations_company=decorations_supplier)
event2 = Event(2, birthday, "Kid's Birthday Party", "2024-06-10", "14:00", "3 hours", venue2, client2,
               catering_company=caterer1, decorations_company=decorations_supplier, entertainment_company=entertainment_supplier)


#creating the GUI
class GUI(tk.Tk):  # Defining a class named GUI which inherits from tk.Tk
    def __init__(self):  # Initializing the GUI class
        super().__init__()  # Calling the constructor of the parent class

        self.title("Event Management System")  # creating the title for the GUI

        # Creating and placing a label widget for user input
        self.label = tk.Label(self, text="Enter ID Number:")
        self.label.grid(row=0, column=0)

        # Creating and placing an entry widget for user input
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1)

        # Creating and placing a button to get employee details
        self.employee_button = tk.Button(self, text="Get Employee Details", command=self.get_employee_details)
        self.employee_button.grid(row=1, column=0, columnspan=2, pady=5)

        # Creating and placing a button to get event details
        self.event_button = tk.Button(self, text="Get Event Details", command=self.get_event_details)
        self.event_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Creating and placing a button to get client details
        self.client_button = tk.Button(self, text="Get Client Details", command=self.get_client_details)
        self.client_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Creating and placing a button to get supplier details
        self.supplier_button = tk.Button(self, text="Get Supplier Details", command=self.get_supplier_details)
        self.supplier_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Creating and placing a button to get guest details
        self.guest_button = tk.Button(self, text="Get Guest Details", command=self.get_guest_details)
        self.guest_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Creating and placing a button to get venue details
        self.venue_button = tk.Button(self, text="Get Venue Details", command=self.get_venue_details)
        self.venue_button.grid(row=6, column=0, columnspan=2, pady=5)

        # Creating and placing a button to add details
        self.add_button = tk.Button(self, text="Add Details", command=self.add_details)
        self.add_button.grid(row=7, column=0, columnspan=2, pady=5)

        # Creating and placing a button to modify details
        self.modify_button = tk.Button(self, text="Modify Details", command=self.modify_details)
        self.modify_button.grid(row=8, column=0, columnspan=2, pady=5)

        # Creating and placing a button to delete details
        self.delete_button = tk.Button(self, text="Delete Details", command=self.delete_details)
        self.delete_button.grid(row=9, column=0, columnspan=2, pady=5)

    def add_details(self):  # Method to add details based on user input
        # Asking user to select the type of details to add
        id_number = simpledialog.askinteger("Add Details","Enter ID Number (0 for Employee, 1 for Event, 2 for Client, 3 for Supplier, 4 for Guest):")
        if id_number is not None:  # Checking if the user has provided an input
            if id_number == 0:  # If user selected to add Employee details
                # Asking user to input employee details
                name = simpledialog.askstring("Add Employee", "Enter Employee Name:")
                emp_id = simpledialog.askinteger("Add Employee", "Enter Employee ID:")
                department = simpledialog.askstring("Add Employee", "Enter Department:")
                job_title = simpledialog.askstring("Add Employee", "Enter Job Title:")
                basic_salary = simpledialog.askfloat("Add Employee", "Enter Basic Salary:")
                manager_id = simpledialog.askinteger("Add Employee", "Enter Manager ID (optional):")
                messagebox.showinfo("Success", "Employee successfully added!")  # Showing success message
            elif id_number == 1:  # If user selected to add Event details
                # Asking user to input event details
                event_id = simpledialog.askinteger("Add Event", "Enter Event ID:")
                client = simpledialog.askstring("Add Client", "Enter Client name:")
                guest = simpledialog.askstring("Add Guest", "Enter Guest name:")
                messagebox.showinfo("Success", "Event successfully added!")  # Showing success message
                pass
            elif id_number == 2:  # If user selected to add Client details
                # Asking user to input client details
                name = simpledialog.askstring("Add Client", "Enter name:")
                client_id = simpledialog.askinteger("Add Client", "Enter Client ID:")
                address = simpledialog.askstring("Add Client", "Enter address:")
                contact = simpledialog.askinteger("Add Client", "Enter contact number:")
                budget = simpledialog.askinteger("Add Client", "Enter budget:")
                messagebox.showinfo("Success", "Client successfully added!")  # Showing success message
                pass
            elif id_number == 3:  # If user selected to add Supplier details
                # Asking user to input supplier details
                name = simpledialog.askstring("Add Supplier", "Enter name:")
                supplier_id = simpledialog.askinteger("Add Supplier", "Enter Supplier ID:")
                address = simpledialog.askstring("Add Supplier", "Enter address:")
                contact = simpledialog.askinteger("Add Supplier", "Enter contact number:")
                messagebox.showinfo("Success", "Supplier successfully added!")  # Showing success message
                pass
            elif id_number == 4:  # If user selected to add Guest details
                # Asking user to input guest details
                name = simpledialog.askstring("Add Guest", "Enter name:")
                guest_id = simpledialog.askstring("Add Guest", "Enter Guest ID:")
                messagebox.showinfo("Success", "Guest successfully added!")  # Showing success message
                pass
            else:
                messagebox.showerror("Error", "Invalid ID")  # Showing error message if ID is invalid

    def modify_details(self):  # Method to modify details based on user input
        id_number = simpledialog.askinteger("Modify Details",
                                            "Enter ID Number (0 for Employee, 1 for Event, 2 for Client, 3 for Supplier, 4 for Guest):")  # Asking user to select the type of details to modify
        if id_number is not None:  # Checking if the user has provided an input
            if id_number == 0:  # If user selected to modify Employee details
                employee_id = simpledialog.askinteger("Modify Employee",
                                                      "Enter Employee ID to Modify:")  # Asking user to input the Employee ID to modify
                if employee_id is not None:  # Checking if the user has provided an input
                    for employee in [susan_meyers, joy_rogers, shyam_sundar, mariam_khalid,
                                     salem_j_sam]:  # Looping through the list of employees
                        if employee.emp_id == employee_id:  # If employee ID matches
                            # Asking user to input updated employee details
                            updated_name = simpledialog.askstring("Modify Employee", "Enter Updated Name:")
                            updated_emp_id = simpledialog.askinteger("Modify Employee", "Enter Updated Employee ID:")
                            updated_department = simpledialog.askstring("Modify Employee", "Enter Updated Department:")
                            updated_job_title = simpledialog.askstring("Modify Employee", "Enter Updated Job Title:")
                            updated_basic_salary = simpledialog.askfloat("Modify Employee",
                                                                         "Enter Updated Basic Salary:")
                            updated_manager_id = simpledialog.askinteger("Modify Employee",
                                                                         "Enter Updated Manager ID (optional):")

                            # Updating employee details
                            employee.name = updated_name
                            employee.emp_id = updated_emp_id
                            employee.department = updated_department
                            employee.job_title = updated_job_title
                            employee.basic_salary = updated_basic_salary
                            employee.manager_id = updated_manager_id

                            messagebox.showinfo("Success",
                                                "Employee details successfully updated!")  # Showing success message
                            return
                    messagebox.showerror("Error", "Employee not found.")  # Showing error message if employee not found
                elif id_number == 1:  # If user selected to modify Event details
                    event_id = simpledialog.askinteger("Modify Event",
                                                       "Enter Event ID to Modify:")  # Asking user to input the Event ID to modify
                    if event_id is not None:  # Checking if the user has provided an input
                        for event in [event1, event2]:  # Looping through the list of events
                            if event.event_id == event_id:  # If event ID matches
                                # Asking user to input updated event details
                                updated_event_type = simpledialog.askstring("Modify Event", "Enter Updated Event Type:")
                                updated_theme = simpledialog.askstring("Modify Event", "Enter Updated Theme:")
                                updated_date = simpledialog.askstring("Modify Event", "Enter Updated Date:")
                                updated_time = simpledialog.askstring("Modify Event", "Enter Updated Time:")
                                updated_duration = simpledialog.askstring("Modify Event", "Enter Updated Duration:")

                                # Updating event details
                                event.event_type.name = updated_event_type
                                event.theme = updated_theme
                                event.date = updated_date
                                event.time = updated_time
                                event.duration = updated_duration
                                messagebox.showinfo("Success",
                                                    "Event details successfully updated!")  # Showing success message
                                return

                        messagebox.showerror("Error", "Event not found.")  # Showing error message if event not found
                pass
            elif id_number == 2:  # If user selected to modify Client details
                client_id = simpledialog.askinteger("Modify Client",
                                                    "Enter Client ID to Modify:")  # Asking user to input the Client ID to modify
                if client_id is not None:  # Checking if the user has provided an input
                    for client in [client1, client2]:  # Looping through the list of clients
                        if client.client_id == client_id:  # If client ID matches
                            # Asking user to input updated client details
                            updated_name = simpledialog.askstring("Modify Client", "Enter Updated Name:")
                            updated_address = simpledialog.askstring("Modify Client", "Enter Updated Address:")
                            updated_contact = simpledialog.askstring("Modify Client", "Enter Updated Contact:")
                            updated_budget = simpledialog.askfloat("Modify Client", "Enter Updated Budget:")

                            # Updating client details
                            client.name = updated_name
                            client.address = updated_address
                            client.contact = updated_contact
                            client.budget = updated_budget

                            messagebox.showinfo("Success",
                                                "Client details successfully updated!")  # Showing success message
                            return
                    messagebox.showerror("Error", "Client not found.")  # Showing error message if client not found
                pass
            elif id_number == 3:  # If user selected to modify Supplier details
                supplier_id = simpledialog.askinteger("Modify Supplier",
                                                      "Enter Supplier ID to Modify:")  # Asking user to input the Supplier ID to modify
                if supplier_id is not None:  # Checking if the user has provided an input
                    for supplier in [catering_supplier, cleaning_supplier, decorations_supplier, entertainment_supplier,
                                     furniture_supplier]:  # Looping through the list of suppliers
                        if supplier.supplier_id == supplier_id:  # If supplier ID matches
                            # Asking user to input updated supplier details
                            updated_name = simpledialog.askstring("Modify Supplier", "Enter Updated Name:")
                            updated_address = simpledialog.askstring("Modify Supplier", "Enter Updated Address:")
                            updated_contact = simpledialog.askstring("Modify Supplier", "Enter Updated Contact:")

                            # Updating supplier details
                            supplier.name = updated_name
                            supplier.address = updated_address
                            supplier.contact = updated_contact

                            messagebox.showinfo("Success",
                                                "Supplier details successfully updated!")  # Showing success message
                            return

                    messagebox.showerror("Error", "Supplier not found.")  # Showing error message if supplier not found
                pass
            elif id_number == 4:  # If user selected to modify Guest details
                guest_id = simpledialog.askinteger("Modify Guest",
                                                   "Enter Guest ID to Modify:")  # Asking user to input the Guest ID to modify
                if guest_id is not None:  # Checking if the user has provided an input
                    for guest in [guest1, guest2]:  # Looping through the list of guests
                        if guest.guest_id == guest_id:  # If guest ID matches
                            # Asking user to input updated guest details
                            updated_name = simpledialog.askstring("Modify Guest", "Enter Updated Name:")
                            guest.name = updated_name

                            messagebox.showinfo("Success",
                                                "Guest details successfully updated!")  # Showing success message
                            return
                    messagebox.showerror("Error", "Guest not found.")  # Showing error message if guest not found
            else:
                messagebox.showerror("Error", "Invalid ID")  # Showing error message if ID is invalid

    def delete_details(self):  #Method to delete details based on user input
        id_number = simpledialog.askinteger("Delete Details",
                                            "Enter ID Number (0 for Employee, 1 for Event, 2 for Client, 3 for Supplier, 4 for Guest):")  # Asking user to select the type of details to delete
        if id_number is not None:  # Checking if the user has provided an input
            if id_number == 0:  # If user selected to delete Employee details
                employee_id = simpledialog.askinteger("Delete Employee",
                                                      "Enter Employee ID to Delete:")  #Asking user to input the Employee ID to delete
                if employee_id is not None:  # Checking if the user has provided an input
                    for index, employee in enumerate([susan_meyers, joy_rogers, shyam_sundar, mariam_khalid,
                                                      salem_j_sam]):  # Looping through the list of employees
                        if employee.emp_id == employee_id:  # If employee ID matches
                            del [susan_meyers, joy_rogers, shyam_sundar, mariam_khalid, salem_j_sam][
                                index]  # Deleting the employee
                            messagebox.showinfo("Success",
                                                "Employee details successfully deleted!")  # Showing success message
                            return
                    messagebox.showerror("Error", "Employee not found.")  # Showing error message if employee not found
                elif id_number == 1:  # If user selected to delete Event details
                    event_id = simpledialog.askinteger("Delete Event",
                                                       "Enter Event ID to Delete:")  # Asking user to input the Event ID to delete
                    if event_id is not None:  # Checking if the user has provided an input
                        for index, event in enumerate([event1, event2]):  # Looping through the list of events
                            if event.event_id == event_id:  # If event ID matches
                                del [event1, event2][index]  # Deleting the event
                                messagebox.showinfo("Success",
                                                    "Event details successfully deleted!")  # Showing success message
                                return
                        messagebox.showerror("Error", "Event not found.")  # Showing error message if event not found
                pass
            elif id_number == 2:  # If user selected to delete Client details
                client_id = simpledialog.askinteger("Delete Client",
                                                    "Enter Client ID to Delete:")  # Asking user to input the Client ID to delete
                if client_id is not None:  # Checking if the user has provided an input
                    for index, client in enumerate([client1, client2]):  # Looping through the list of clients
                        if client.client_id == client_id:  # If client ID matches
                            del [client1, client2][index]  # Deleting the client
                            messagebox.showinfo("Success",
                                                "Client details successfully deleted!")  # Showing success message
                            return
                    messagebox.showerror("Error", "Client not found.")  # Showing error message if client not found
            elif id_number == 3:  # If user selected to delete Supplier details
                supplier_id = simpledialog.askinteger("Delete Supplier",
                                                      "Enter Supplier ID to Delete:")  # Asking user to input the Supplier ID to delete
                if supplier_id is not None:  # Checking if the user has provided an input
                    for index, supplier in enumerate(
                            [catering_supplier, cleaning_supplier, decorations_supplier, entertainment_supplier,
                             furniture_supplier]):  # Looping through the list of suppliers
                        if supplier.supplier_id == supplier_id:  # If supplier ID matches
                            del [catering_supplier, cleaning_supplier, decorations_supplier, entertainment_supplier,
                                 furniture_supplier][index]  # Deleting the supplier
                            messagebox.showinfo("Success",
                                                "Supplier details successfully deleted!")  # Showing success message
                            return
                    messagebox.showerror("Error", "Supplier not found.")  # Showing error message if supplier not found
            elif id_number == 4:  # If user selected to delete Guest details
                guest_id = simpledialog.askinteger("Delete Guest",
                                                   "Enter Guest ID to Delete:")  # Asking user to input the Guest ID to delete
                if guest_id is not None:  # Checking if the user has provided an input
                    for index, guest in enumerate([guest1, guest2]):  # Looping through the list of guests
                        if guest.guest_id == guest_id:  # If guest ID matches
                            del [guest1, guest2][index]  # Deleting the guest
                            messagebox.showinfo("Success",
                                                "Guest details successfully deleted!")  # Showing success message
                            return
                    messagebox.showerror("Error", "Guest not found.")  # Showing error message if guest not found
            else:
                messagebox.showerror("Error", "Invalid ID")  # Showing error message if ID is invalid

    def get_employee_details(self):  # Method to get employee details based on user input
        employee_id = int(self.id_entry.get())  # Retrieving the employee ID entered by the user
        for employee in [susan_meyers, joy_rogers, shyam_sundar, mariam_khalid,
                         salem_j_sam]:  # Looping through the list of employees
            if employee.emp_id == employee_id:  # If employee ID matches
                messagebox.showinfo("Employee Details",
                                    f"Name: {employee.name}\nID: {employee.emp_id}\nDepartment: {employee.department}\nJob Title: {employee.job_title}\nBasic Salary: {employee.basic_salary}")  # Displaying employee details
                return
        messagebox.showerror("Error", "Employee not found.")  # Showing error message if employee not found

    def get_event_details(self):  # Method to get event details based on user input
        event_id = int(self.id_entry.get())  # Retrieving the event ID entered by the user
        for event in [event1, event2]:  # Looping through the list of events
            if event.event_id == event_id:  # If event ID matches
                messagebox.showinfo("Event Details",
                                    f"Event ID: {event.event_id}\nEvent Type: {event.event_type.name}\nTheme: {event.theme}\nDate: {event.date}\nTime: {event.time}\nDuration: {event.duration}\nVenue: {event.venue.name}\nClient: {event.client.name}")  # Displaying event details
                return
        messagebox.showerror("Error", "Event not found.")  # Showing error message if event not found

    def get_client_details(self):  # Method to get client details based on user input
        client_id = int(self.id_entry.get())  # Retrieving the client ID entered by the user
        for client in [client1, client2]:  # Looping through the list of clients
            if client.client_id == client_id:  # If client ID matches
                messagebox.showinfo("Client Details",
                                    f"Name: {client.name}\nClient ID: {client.client_id}\nAddress: {client.address}\nContact: {client.contact}\nBudget: {client.budget}")  # Displaying client details
                return
        messagebox.showerror("Error", "Client not found.")  # Showing error message if client not found

    def get_supplier_details(self):  # Method to get supplier details based on user input
        supplier_id = int(self.id_entry.get())  # Retrieving the supplier ID entered by the user
        for supplier in [catering_supplier, cleaning_supplier, decorations_supplier, entertainment_supplier,
                         furniture_supplier]:  # Looping through the list of suppliers
            if supplier.supplier_id == supplier_id:  # If supplier ID matches
                messagebox.showinfo("Supplier Details",
                                    f"Name: {supplier.name}\nSupplier ID: {supplier.supplier_id}\nAddress: {supplier.address}\nContact: {supplier.contact}")  # Displaying supplier details
                return
        messagebox.showerror("Error", "Supplier not found.")  # Showing error message if supplier not found

    def get_guest_details(self):  # Method to get guest details based on user input
        guest_id = int(self.id_entry.get())  # Retrieving the guest ID entered by the user
        for guest in [guest1, guest2]:  # Looping through the list of guests
            if guest.guest_id == guest_id:  # If guest ID matches
                messagebox.showinfo("Guest Details",
                                    f"Name: {guest.name}\nGuest ID: {guest.guest_id}")  # Displaying guest details
                return
        messagebox.showerror("Error", "Guest not found.")  # Showing error message if guest not found

    def get_venue_details(self):  # Method to get venue details based on user input
        venue_id = int(self.id_entry.get())  # Retrieving the venue ID entered by the user
        for venue in [venue1, venue2]:  # Looping through the list of venues
            if venue.venue_id == venue_id:  # If venue ID matches
                messagebox.showinfo("Venue Details",
                                    f"Name: {venue.name}\nVenue ID: {venue.venue_id}\nAddress: {venue.address}\nContact: {venue.contact}\nMin Guests: {venue.min_guests}\nMax Guests: {venue.max_guests}")  # Displaying venue details
                return
        messagebox.showerror("Error", "Venue not found.")  # Showing error message if venue not found

if __name__ == "__main__":
    app = GUI() #creating an isntance of the GUI class
    app.mainloop() #running the GUI


