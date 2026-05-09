medicines = []
suppliers = []
sales = []

def add_medicine():
    med = {
        "id": input("Medicine ID: "),
        "name": input("Medicine Name: "),
        "price": int(input("Price: ")),
        "qty": int(input("Quantity: ")),
        "expiry": input("Expiry Date: ")
    }
    medicines.append(med)
    print("Medicine added successfully!")

def search_medicine():
    name = input("Enter Medicine Name: ")
    for m in medicines:
        if m["name"] == name:
            print(m)
            return
    print("Medicine not found!")

def update_medicine():
    mid = input("Enter Medicine ID: ")
    for m in medicines:
        if m["id"] == mid:
            p = input("New Price: ")
            q = input("New Quantity: ")
            if p:
                m["price"] = int(p)
            if q:
                m["qty"] = int(q)
            print("Medicine updated!")
            return
    print("Medicine not found!")

def add_supplier():
    sup = {
        "id": input("Supplier ID: "),
        "name": input("Supplier Name: "),
        "contact": input("Contact: "),
        "company": input("Company: ")
    }
    suppliers.append(sup)
    print("Supplier added!")

def total_sale():
    mid = input("Medicine ID: ")
    qty = int(input("Quantity Sold: "))
    for m in medicines:
        if m["id"] == mid and m["qty"] >= qty:
            m["qty"] -= qty
            sale = qty * m["price"]
            sales.append(sale)
            print("Total Sale: ₹", sale)
            return
    print("Not enough stock!")

def monthly_sales():
    print("Monthly Sales: ₹", sum(sales))

while True:
    print("\n===== Pharmacy Inventory System =====")
    print("1.Add Medicine")
    print("2.Search Medicine")
    print("3.Update Medicine")
    print("4.Add Supplier")
    print("5.Calculate Total Sale")
    print("6.Calculate Monthly Sales")
    print("7.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_medicine()
    elif ch == "2":
        search_medicine()
    elif ch == "3":
        update_medicine()
    elif ch == "4":
        add_supplier()
    elif ch == "5":
        total_sale()
    elif ch == "6":
        monthly_sales()
    elif ch == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")