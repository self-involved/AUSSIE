from config import database_management

def gen_id(  ):
    import datetime
    today = str(datetime.date.today())
    day = ''.join(today.split('-'))
    import random
    id1 = random.randint(10, 99)
    id2 = random.randint(10, 99)
    id = day + str(id1) + str(id2)
    return id

def create_customer( *args ):
    con=database_management.connect()
    sql = '''
    insert into customers ( customer_id,name,addr,tel ) values ( %s,%s,%s,%s );
    '''
    id =gen_id()
    name = args[0]
    addr = args[1]
    tel = args[2]

    cur = con.cursor()
    try:
        cur.execute(sql,( id,name,addr,tel ))
        con.commit()
    except:
        print('ERROR\n')
    finally:
        cur.close()
        con.close()

def create_orders( *args ):
    con=database_management.connect()
    sql = '''
    insert into orders ( order_id,customer_id,products,price_in,price_out,method,purchase_date ) values ( %s,%s,%s,%s,%s,%s,%s );
    '''
    sql1 = '''
    insert into logistics ( order_id,customer_id ) values ( %s,%s );
    '''
    id =gen_id()
    customer_id=args[0]
    products=args[1]
    price_in=args[2]
    price_out=args[3]
    method=args[4]
    purchase_date=args[5]

    cur = con.cursor()
    try:
        cur.execute(sql, (id, customer_id,products,price_in,price_out,method,purchase_date))
        cur.execute(sql1, (id, customer_id))
        con.commit()
    except:
        print('ERROR\n')
    finally:
        cur.close()
        con.close()


def update_logistics( *args ):
    con=database_management.connect()
    order_id = args[0]
    send_date=args[1]
    expense =args[2]
    company = args[3]
    logistics_id =args[4]
    verifyed =args[5]
    received =args[6]
    sql = '''
        UPDATE logistics SET send_date='{1}',expense='{2}',company='{3}',logistic_id='{4}',verified='{5}',received='{6}'
        WHERE order_id = '{0}';
        '''.format( order_id,send_date,expense,company,logistics_id,verifyed,received )
    #print(sql)
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except Exception as e:
        print('ERROR\n')
        print('the reason is '+e)
    finally:
        cur.close()
        con.close()

def today():
    import datetime
    today = str(datetime.date.today())
    return today
