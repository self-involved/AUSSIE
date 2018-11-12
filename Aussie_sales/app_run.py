from flask import Flask
import auth.Auth as Auth
import main.Aussie_sales as Aussie_sales

app = Flask( __name__ )
app.register_blueprint( Auth.admin,url_prefix='/auth' )
app.register_blueprint( Aussie_sales.main,url_prefix='/main/admin/auth' )
app.run('0.0.0.0',port=5500,threaded=True)