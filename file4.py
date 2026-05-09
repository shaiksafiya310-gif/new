medicines = []

def add_medicine():
    medicines.append({
        "id": input("Medicine ID: "),
        "name": input("Medicine Name: "),
        "price": int(input("Price: ")),
        "qty": int(input("Quantity: "))
    })
    print("Medicine Added")

def search():
    mid = input("Enter Medicine ID: ")
    for m in medicines:
        if m["id"] == mid:
            print(m)
            return
    print("Medicine not found")

def update():
    mid = input("Enter Medicine ID: ")
    for m in medicines:
        if m["id"] == mid:
            m["price"] = int(input("New Price: "))
            m["qty"] = int(input("New Quantity: "))
            print("Updated")
            return

def generate_bill():
    customer = input("Customer Name: ")
    n = int(input("Number of medicines: "))
    total = 0
    bill = []

    for i in range(n):
        mid = input("Medicine ID: ")
        qty = int(input("Quantity: "))

        for m in medicines:
            if m["id"] == mid:
                if m["qty"] >= qty:
                    amount = qty * m["price"]
                    m["qty"] -= qty
                    total += amount
                    bill.append([m["name"], qty, m["price"], amount])
                else:
                    print("Not enough stock")

    print("\nCustomer Bill -", customer)
    print("----------------------------------------")
    print("Medicine   Qty   Price   Total")

    for b in bill:
        print(b[0], b[1], b[2], b[3])

    print("----------------------------------------")
    print("Grand Total: ₹", total)

while True:
    print("\n1.Add Medicine")
    print("2.Search")
    print("3.Update")
    print("4.Generate Bill")
    print("5.Exit")

    ch = input("Choice: ")

    if ch == "1":
        add_medicine()
    elif ch == "2":
        search()
    elif ch == "3":
        update()
    elif ch == "4":
        generate_bill()
    elif ch == "5":
        break
    else:
        print("Invalid Choice")