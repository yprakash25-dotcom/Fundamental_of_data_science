"""Program to capture sales data, save it to a CSV file, and display total revenue."""

import csv


def write_sales_csv(filename: str, records: list[dict[str, str]]) -> None:
    """Write sales records to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["product", "quantity", "price"])
        writer.writeheader()
        for record in records:
            writer.writerow(record)


def read_sales_csv(filename: str) -> list[dict[str, str]]:
    """Read sales records from a CSV file."""
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def calculate_total_sales(records: list[dict[str, str]]) -> float:
    """Calculate total revenue from sales records."""
    total = 0.0
    for record in records:
        quantity = int(record["quantity"])
        price = float(record["price"])
        total += quantity * price
    return total


def display_sales(records: list[dict[str, str]]) -> None:
    """Print the sales records with formatted columns."""
    print("\nSales records:")
    print("Product\tQuantity\tPrice\tSubtotal")
    print("-------\t--------\t-----\t--------")
    for record in records:
        product = record["product"]
        quantity = int(record["quantity"])
        price = float(record["price"])
        subtotal = quantity * price
        print(f"{product}\t{quantity}\t{price:.2f}\t{subtotal:.2f}")


if __name__ == "__main__":
    print("Sales CSV IO Program")
    records: list[dict[str, str]] = []

    for i in range(1, 4):
        print(f"\nEnter data for item {i}:")
        product = input("Product name: ").strip()
        quantity = input("Quantity: ").strip()
        price = input("Price per item: ").strip()
        records.append({"product": product, "quantity": quantity, "price": price})

    filename = "sales.csv"
    write_sales_csv(filename, records)
    print(f"\nSales data saved to {filename}.")

    saved_records = read_sales_csv(filename)
    display_sales(saved_records)
    print(f"\nTotal revenue: {calculate_total_sales(saved_records):.2f}")
