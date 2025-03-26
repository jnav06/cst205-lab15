# GITHUB LINK: https://github.com/jnav06/cst205-lab15

from flask import Flask

app = Flask(__name__)

@app.route('/')

def main(): # I was not in class on Monday :( so i am reusing some old fun facts from lab 1
  return """

    <html>
    
        <head>
            <title>Lab 15 ~ Task 2</title>
        </head>
        
        <body>
            <p>Fun facts:</p>
            <p></p>
            
            <p>Ulises - he enjoys skating in his free time</p>
            <p>Lorenzo - he has been working on an emulation machine using Raspberry Pi</p>
            <p>Thomas - he enjoys playing video games sometimes</p>
        </body>

    </html>

  """

if __name__ == "__main__":
    app.run(debug = True)