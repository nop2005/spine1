from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>คำนวณภาษี 7%</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 500px;
            width: 100%;
        }
        
        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2em;
        }
        
        .form-group {
            margin-bottom: 25px;
        }
        
        label {
            display: block;
            color: #333;
            font-weight: 600;
            margin-bottom: 8px;
            font-size: 1.1em;
        }
        
        input[type="number"] {
            width: 100%;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1.1em;
            transition: all 0.3s;
        }
        
        input[type="number"]:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        button {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.2em;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        .result {
            margin-top: 30px;
            padding: 25px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 15px;
            border-left: 5px solid #667eea;
        }
        
        .result h2 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.5em;
        }
        
        .result-item {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        }
        
        .result-item:last-child {
            border-bottom: none;
            font-weight: 700;
            font-size: 1.2em;
            color: #667eea;
            margin-top: 10px;
            padding-top: 15px;
            border-top: 2px solid #667eea;
        }
        
        .result-label {
            color: #555;
        }
        
        .result-value {
            color: #333;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🧮 คำนวณภาษี 7%</h1>
        
        <form method="POST">
            <div class="form-group">
                <label for="price">ราคาสินค้า (บาท):</label>
                <input type="number" id="price" name="price" step="0.01" 
                       placeholder="กรอกราคาสินค้า" required 
                       value="{{ price if price else '' }}">
            </div>
            
            <button type="submit">คำนวณ</button>
        </form>
        
        {% if result %}
        <div class="result">
            <h2>📊 ผลการคำนวณ</h2>
            <div class="result-item">
                <span class="result-label">ราคาสินค้า:</span>
                <span class="result-value">{{ "%.2f"|format(result.price) }} บาท</span>
            </div>
            <div class="result-item">
                <span class="result-label">ภาษี (7%):</span>
                <span class="result-value">{{ "%.2f"|format(result.tax) }} บาท</span>
            </div>
            <div class="result-item">
                <span class="result-label">ราคารวมภาษี:</span>
                <span class="result-value">{{ "%.2f"|format(result.total) }} บาท</span>
            </div>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    price = None
    
    if request.method == 'POST':
        try:
            price = float(request.form.get('price', 0))
            tax = price * 0.07
            total = price + tax
            
            result = {
                'price': price,
                'tax': tax,
                'total': total
            }
        except ValueError:
            result = None
    
    return render_template_string(HTML_TEMPLATE, result=result, price=price)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)