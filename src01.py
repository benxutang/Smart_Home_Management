import connexion

app = connexion.App(__name__, specification_dir='./')
#app.add_api('swagger.yml')
app.add_api('swaggerfull.yml')

# @app.before_request
# def before_request():
#     if not request.is_secure and app.env != "development":
#         url = request.url.replace("http://", "https://", 1)
#         code = 301
#         return redirect(url, code=code)

@app.route('/')
def index():
	return 'index'



# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', ssl_context=('/etc/httpd/ssl/2_nussh.happydoudou.xyz.crt','/etc/httpd/ssl/3_nussh.happydoudou.xyz.key'),port=5000, debug=True)
