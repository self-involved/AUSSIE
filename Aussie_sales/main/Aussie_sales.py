from flask import Flask,Blueprint,render_template,request,redirect,url_for
main = Blueprint('main', __name__,
                  template_folder='/Users/xiaoking/PycharmProjects/Aussie_sales/templates',
                  static_folder='/Users/xiaoking/PycharmProjects/Aussie_sales/static',)


@main.route('/create/',methods=['POST','GET'])
def create_customers( ):
    return render_template('create.html')

#这个页面还没做好
@main.route('/create/view/',methods=['POST','GET'])
def view_customers( ):
    from config import search_data
    content = search_data.show_customers()
    print(content)
    return render_template('show_customer.html',result=content)

#这个页面还没做好
@main.route('/create/add/',methods=['POST','GET'])
def add_customers( ):
    if request.method=='GET':
        name=request.args.get('name','')
        addr=request.args.get('addr','')
        tel=request.args.get('tel','')
        from config import insert_data
        insert_data.create_customer(name,addr,tel)
        return name+' '+addr+' '+tel+' have been saved!'
    else:
        return 'ERROR'


@main.route('/order/',methods=['POST','GET'])
def update_order( ):
    from config import insert_data
    today = insert_data.today()
    from config import search_data
    result = search_data.select_customers()
    return render_template('order.html',today=today,content=result)

@main.route('/order/create',methods=['POST','GET'])
def update_order_next( ):
    if request.method=='GET':
        customer=request.args.get('customer','')
        customer_id = customer.split(' ')[0]
        item=request.args.get('item','')
        spend=request.args.get('spend','')
        earn=request.args.get('earn','')
        sale_method=request.args.get('sale_method','')
        purchase_date=request.args.get('purchase_date','')
        from config import insert_data
        insert_data.create_orders( customer_id,item,spend,earn,sale_method,purchase_date )
        return 'the data of '+customer+' has been saaved'
    else:
        return 'ERROR'



#这个页面还没做好
@main.route('/logistics/',methods=['POST','GET'])
def update_logistics( ):
    from config import insert_data,search_data
    today = insert_data.today()
    content=search_data.select_orders()
    return render_template('logistic_update.html',today=today,content=content)


@main.route('/logistics/update',methods=['POST','GET'])
def update_logistics_next( ):
    if request.method=='GET':
        order=request.args.get('order_list','')
        print(order)
        order_id = order.split(' ')[0]
        delivery=request.args.get('delivery','')
        company=request.args.get('company','')
        id=request.args.get('id','')
        send_date=request.args.get('send_date','')
        verified=request.args.get('verified','')
        received=request.args.get('received','')
        from config import insert_data
        insert_data.update_logistics( order_id,send_date,delivery,company,id,verified,received )
        return 'the data of '+order_id+' has been saaved'
    else:
        return 'ERROR'
