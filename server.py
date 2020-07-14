from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')
#dyamic page call
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# database code
def write_to_file(data):
	with open('database.csv', mode='a') as database:
	 email=data["email"]
	 subject=data["subject"]
	 message=data["message"]
	 file=database.write(f'\n {email} ,{subject},{message}')

def write_to_csv(data):
	with open('database.csv',newline='', mode='a') as database2:
	 email=data["email"]
	 subject=data["subject"]
	 message=data["message"]
	 csv_writer=csv.writer(database2,delimiter=',' ,  quotechar='|' ,quoting=csv.QUOTE_MINIMAL)
	 csv_writer.writerow([email ,subject,message])

#submitting a form
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		data=request.form.to_dict()
		write_to_file(data)
		write_to_csv(data)
		print(data)
		return redirect('/thankyou.html')
	else:
		return 'Something went wrong'
		









# @app.route('/components')
# def my_component():
#     return render_template('components.html')

# @app.route('/contact')
# def my_contact():
#     return render_template('contact.html')

# @app.route('/work')
# def my_work():
#     return render_template('work.html')
# @app.route('/works')
# def my_works():
#     return render_template('works.html')
