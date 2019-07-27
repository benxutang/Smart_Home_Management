import connexion

app = connexion.App(__name__, specification_dir='./')
#app.add_api('swagger.yml')
app.add_api('swaggerfull.yml')



@app.route('/')
def index():
	return 'index'



# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
