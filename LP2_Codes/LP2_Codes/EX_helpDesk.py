tickets = []

def create_ticket(ticket_id, title, description):
    ticket = {
        "ticket_id": ticket_id,
        "title": title,
        "description": description,
        "status": "Open"
    }
    tickets.append(ticket)
    print("Ticket created successfully.")

def view_tickets():
    if not tickets:
        print("No tickets available.")
    else:
        print("All Tickets:")
        for ticket in tickets:
            print("Ticket ID: ",ticket['ticket_id'])
            print("Title: ",ticket['title'])
            print("Description: ",ticket['description'])
            print("Status: ",ticket['status'])
            print("-------------------------")

def update_ticket_status(ticket_id, status):
    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            ticket["status"] = status
            print("Ticket status updated successfully.")
            return
    print("Ticket not found.")

def delete_ticket(ticket_id):
    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            tickets.remove(ticket)
            print("Ticket deleted successfully.")
            return
    print("Ticket not found.")

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. Create a ticket")
        print("2. View all tickets")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            ticket_id = input("Enter ticket ID: ")
            title = input("Enter ticket title: ")
            description = input("Enter ticket description: ")
            create_ticket(ticket_id, title, description)

        elif choice == "2":
            view_tickets()

        elif choice == "3":
            print("Exiting the customer menu...")
            break

        else:
            print("Invalid choice. Please try again.")

def manager_menu():
    while True:
        print("\n--- Manager Menu ---")
        print("1. View all tickets")
        print("2. Update ticket status")
        print("3. Delete a ticket")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tickets()

        elif choice == "2":
            ticket_id = input("Enter ticket ID to update status: ")
            status = input("Enter new status: ")
            update_ticket_status(ticket_id, status)

        elif choice == "3":
            ticket_id = input("Enter ticket ID to delete: ")
            delete_ticket(ticket_id)

        elif choice == "4":
            print("Exiting the manager menu...")
            break

        else:
            print("Invalid choice. Please try again.")

def menu():
    while True:
        print("\n--- Helpdesk Management System ---")
        print("1. Customer Menu")
        print("2. Manager Menu")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            customer_menu()

        elif choice == "2":
            manager_menu()

        elif choice == "3":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

menu()
