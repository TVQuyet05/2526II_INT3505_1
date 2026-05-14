from flask import Flask, request, jsonify

app = Flask(__name__)

# Dữ liệu tĩnh giả lập Database
products = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 1200},
    {"id": 2, "name": "Mouse", "category": "electronics", "price": 25},
    {"id": 3, "name": "Desk", "category": "furniture", "price": 150},
    {"id": 4, "name": "Chair", "category": "furniture", "price": 85},
    {"id": 5, "name": "Headphones", "category": "electronics", "price": 100}
]

@app.route('/products', methods=['GET'])
def search_products():
    # Nhận các tham số Query (Query Parameters) từ URL
    category = request.args.get('category')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    sort_by = request.args.get('sort')
    limit = request.args.get('limit', type=int)
    
    result = products
    
    # Lọc (Filtering) - Lọc theo Category
    if category:
        result = [p for p in result if p['category'] == category]
        
    # Lọc (Filtering) - Lọc theo Giá
    if min_price is not None:
        result = [p for p in result if p['price'] >= min_price]
    if max_price is not None:
        result = [p for p in result if p['price'] <= max_price]
        
    # Sắp xếp (Sorting)
    if sort_by == 'price_asc':
        result = sorted(result, key=lambda x: x['price'])
    elif sort_by == 'price_desc':
        result = sorted(result, key=lambda x: x['price'], reverse=True)
        
    # Phân trang/Giới hạn (Pagination/Limit)
    if limit:
        result = result[:limit]

    return jsonify({
        "metadata": {
            "total_matches": len(result),
            "filters_applied": {
                "category": category,
                "min_price": min_price,
                "max_price": max_price,
                "sort": sort_by,
                "limit": limit
            }
        },
        "data": result
    }), 200

if __name__ == '__main__':
    print("Starting Query API on port 5003...")
    print("Try: GET http://localhost:5003/products?category=electronics&max_price=200&sort=price_desc")
    app.run(port=5003)