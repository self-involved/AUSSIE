from config import database_management


def create_tables( ):
    con = database_management.connect()
    cur = con.cursor()
    customer_sql ='''
        create table customers
        (
        customer_id varchar(14) not null ,
        name varchar(40) not null,
        addr varchar(100) not null,
        tel varchar(20) not null,
        primary key(customer_id)
        )
        ENGINE=INNODB, CHARSET='utf8mb4';
        '''

    order_sql = '''
        create table orders
        (
        order_id varchar(14) not null,
        customer_id varchar(14) not null,
        products varchar(100),
        price_in float not NULL,
        price_out float not NULL,
        method varchar(10) default 'Alipay',
        purchase_date DATE not NULL ,
        primary key(order_id)
        )
        ENGINE=INNODB, CHARSET='utf8mb4';
        '''

    logistics_sql = '''
            create table logistics
            (
            order_id varchar(14) not null,
            customer_id varchar(14) not null,
            send_date DATE default NULL,
            expense float default 0,
            company varchar(20) default '长江',
            logistic_id varchar(30) default Null,
            verified BOOLEAN default FALSE,
            received  BOOLEAN default FALSE,
            primary key(order_id)
            )
            ENGINE=INNODB, CHARSET='utf8mb4';
            '''

    cur.execute(customer_sql)
    con.commit()
    cur.execute(order_sql)
    con.commit()
    cur.execute(logistics_sql)
    con.commit()
    cur.close()
    con.close()

if __name__=='__main__':
    create_tables()
