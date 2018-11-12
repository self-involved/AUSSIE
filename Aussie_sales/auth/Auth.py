from flask import Flask,Blueprint,render_template,request,redirect,url_for
admin = Blueprint('admin', __name__,
                  template_folder='/Users/xiaoking/PycharmProjects/Aussie_sales/templates',
                  static_folder='/Users/xiaoking/PycharmProjects/Aussie_sales/static',)


@admin.route('/')
def admin_login( ):
    return render_template( 'login_page.html' )

@admin.route('/login/',methods=['POST','GET'])
def login( ):
    if request.method=='GET':
        name = request.args.get('admin_name','')
        pwd = request.args.get('password','')
        if (name=='admin' and pwd=='admin'):
            return render_template( 'welcome.html' )
        else:
            return redirect(url_for('admin.admin_login'))
    else:
        return redirect( url_for('admin.admin_login') )

