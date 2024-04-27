from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 報告書のリストを格納するリスト
reports = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_report', methods=['POST'])
def new_report():
    title = request.form['report-title']
    date = request.form['report-date']
    content = request.form['report-content']

    report = {'title': title, 'date': date, 'content': content}
    reports.append(report)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
