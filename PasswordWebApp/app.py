from flask import Flask, render_template, request
from checker.strength_checker import check_password_strength
from checker.password_generator import generate_password

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    generated_password = ""

    if request.method == 'POST':
        if 'check' in request.form:
            password = request.form['password']
            strength, remarks = check_password_strength(password)
            messages = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
            color = ["danger", "warning", "secondary", "info", "success"]
            result = {
                'message': messages[strength],
                'remarks': remarks,
                'color': color[strength]
            }

        elif 'generate' in request.form:
            length = int(request.form.get('length', 12))
            use_special = 'special' in request.form
            generated_password = generate_password(length, use_special)

    return render_template('index.html', result=result, generated_password=generated_password)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=9000, debug=True)