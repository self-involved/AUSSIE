from config import database_management

def show_customers(  ):
    con=database_management.connect()
    cur=con.cursor()
    sql='''
    select * from customers;
    '''
    cur.execute(sql)
    result = cur.fetchall()
    return result

def select_customers(  ):
    con=database_management.connect()
    cur=con.cursor()
    sql='''
    select * from customers;
    '''
    cur.execute(sql)
    result = cur.fetchall()
    modified=[]
    for each in result:
        modified.append( ' '.join(each) )
    return modified



def select_orders(  ):
    con=database_management.connect()
    cur=con.cursor()
    sql='''
    select a.order_id,c.name,b.products,b.purchase_date from logistics a,orders b,customers c
     where a.order_id=b.order_id and a.customer_id=c.customer_id and a.received=FALSE;
    '''
    cur.execute(sql)
    result = cur.fetchall()
    modified=[]
    for each in result:
        temp=''
        for i in each:
            try:
                temp=temp+' '+i
            except:
                temp = temp + ' ' + i.strftime( '%Y-%m-%d' )
        modified.append(temp)
    return modified

