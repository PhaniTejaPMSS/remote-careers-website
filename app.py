from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'New Delhi, India',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'Frontend Developer',
  'location': 'Chennai, India',
  'salary': 'Rs. 8,00,000'
}, {
  'id': 4,
  'title': 'Backend Developer',
  'location': 'New Jersey, USA',
  'salary': '$ 120,000'
}]


@app.route("/")
def start():
  return render_template('index.html', jobs=JOBS, company_name='ProSurge')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  # print("Hi, there")
  app.run(host="0.0.0.0", debug=True)
