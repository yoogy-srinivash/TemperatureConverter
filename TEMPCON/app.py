from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            celsius_str = request.form.get('celsius')
            if celsius_str:
                celsius = float(celsius_str)
                fahrenheit = (celsius * 9/5) + 32
                result = {'celsius': celsius, 'fahrenheit': round(fahrenheit, 2)}
            else:
                error = "Please enter a temperature value"
        except ValueError:
            error = "Please enter a valid number"
    
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)