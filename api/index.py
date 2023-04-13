from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/reverse" method="post">
            <input type="text" name="string">
            <input type="submit" value="Reverse">
        </form>
    '''

@app.route('/reverse', methods=['POST'])
def reverse_string():
    input_string = request.form['string']
    reversed_string = input_string[::-1]
    return f'''
        <p>Original string: {input_string}</p>
        <p>Reversed string: {reversed_string}</p>
        <button><a href="/" style="text-decoration: none;">Back</a></button>
    '''

if __name__ == '__main__':
    app.run()
