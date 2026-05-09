medicines = [
    {"id": "M101", "name": "Paracetamol", "price": 20, "qty": 100},
    {"id": "M103", "name": "Cough Syrup", "price": 80, "qty": 50}
]

def generate_bill():
    customer = input("Enter Customer Name: ")
    n = int(input("Enter number of medicines: "))
    bill = []
    total = 0

    for i in range(n):
        mid = input("Enter Medicine ID: ")
        qty = int(input("Enter Quantity: "))

        for m in medicines:
            if m["id"] == mid and m["qty"] >= qty:
                amount = qty * m["price"]
                m["qty"] -= qty
                total += amount
                bill.append([m["name"], qty, m["price"], amount])

    discount = 0
    ans = input("Do you want discount? (yes/no): ")

    if ans == "yes":
        dtype = input("Enter discount type (percent/flat): ")
        value = int(input("Enter discount value: "))

        if dtype == "percent":
            discount = total * value / 100
        else:
            discount = value

    grand_total = total - discount

    print("\nCustomer Bill -", customer)
    print("--------------------------------------")
    print("Medicine   Qty   Price   Total")

    for b in bill:
        print(b[0], b[1], "₹"+str(b[2]), "₹"+str(b[3]))

    print("--------------------------------------")
    print("Sub Total: ₹", total)
    print("Discount: -₹", discount)
    print("Grand Total: ₹", grand_total)
    print("Sale recorded successfully!")

generate_bill()