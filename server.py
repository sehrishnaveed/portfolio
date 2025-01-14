from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/work<int:page_number>.html")
def work(page_number):
    return render_template('work.html', page_number=page_number)

@app.route("/<string:page_name>")
def works(page_name):
    return render_template(page_name)


def write_to_file(data):
    try:
        with open('webserver/database.txt', mode='a') as my_file:
            email = data['email']
            subject = data['subject']
            message = data['message']
            my_file.write(f'\n{email},{subject},{message}')
    except FileNotFoundError as err:
        print('File is not found')
    except PermissionError as err:
        print('Permission denied')
    except Exception as e:
        print('Error occurred', e)

def write_to_csv(data):
    try:
        with open('webserver/database.csv', mode='a', newline='\n') as database:
            email = data['email']
            subject = data['subject']
            message = data['message']
            csvwriter = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow([email,subject,message])
    except FileNotFoundError as err:
        print('File is not found')
    except PermissionError as err:
        print('Permission denied')
    except Exception as e:
        print('Error occurred', e)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong!'