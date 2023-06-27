# print('Om Gam Ganapathaye Namaha:')

from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
  return "Om Gam Ganapathaye Namaha:"

if __name__ == "__main__":
  # print("Hi, there")
  app.run(host="0.0.0.0", debug=True)
