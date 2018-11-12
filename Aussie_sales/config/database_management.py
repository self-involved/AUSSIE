import pymysql

def connect():
    connection = pymysql.connect(host='ec2db.cmvp0kxmic2d.ap-southeast-2.rds.amazonaws.com', port=3306, user='bahamutedean', passwd='jx13805152868',
                             db='Aussie',charset='utf8' )
    return connection

