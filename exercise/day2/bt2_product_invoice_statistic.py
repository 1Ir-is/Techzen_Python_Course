# Mỗi sản phẩm là 1 tuple (product_id, name, price)
products = [
    (1, "Ban Phim", 250_000),
    (2, "Chuot", 150_000),
    (3, "Man Hinh", 3_000_000),
    (4, "Tai Nghe", 500_000),
]

# Danh sách đơn hàng (list dict)
orders = [
    {"order_id": "HD01", "items": [1, 2, 4]},
    {"order_id": "HD02", "items": [2, 3]},
    {"order_id": "HD03", "items": [1, 4]},
]

#Cau a: Tạo một dict `product_map` từ `products` để tra cứu nhanh theo `product_id`
product_map = {}
for product_id, name, price in products:
    product_map[product_id] = {"name": name, "price": price}

#Cau b: Với mỗi hóa đơn trong `orders`, hãy tính tổng tiền của hóa đơn đó, lưu vào key mới `"total"` trong từng dict hóa đơn
for order in orders:
    total = 0
    for product_id in order.get("items", []):
        price = product_map.get(product_id, {}).get("price", 0)
        total += price
    order["total"] = total
print("Danh sach hoa don sau khi tinh toan tong tien:")
for order in orders:
    print(f"Order ID: {order.get('order_id')}, Total: {order.get('total')}")    
print()


#Cau c: In ra danh sách hóa đơn theo format:
for order in orders:
    order_id = order.get("order_id", "")
    items = order.get("items", [])
    num_items = len(items)
    total = order.get("total", 0)
    print(f"{order_id}: {num_items} san phan, Tong tien: {total}")


#Cau d: Tạo một set `all_products_sold` chứa tất cả `product_id` đã từng được bán trong mọi hóa đơn,
all_products_sold = set()
for order in orders:
    for product_id in order.get("items", []):
        all_products_sold.add(product_id)

print()
print(f"So luong san pham khac nhau da ban: {len(all_products_sold)}")