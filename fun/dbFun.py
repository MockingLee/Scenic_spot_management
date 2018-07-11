import pymysql

db = pymysql.connect("45.76.223.233", "root", "root", "scenic")
cursor = db.cursor()



def inserNode(name,popularity,description,rest_zone,toilet):
    sql = 'insert into scenic_spot values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')'% (name,popularity,description,rest_zone,toilet)
    cursor.execute(sql)
    db.commit()

def deleteNode(name):
    sql = 'delete from scenic_spot where name = \'%s\'' %name
    cursor.execute(sql)
    db.commit()

def inserEdge(name1,name2,weight):
    sql = 'insert into edge values(\'%s\',\'%s\',\'%s\')' %(name1,name2,weight)
    cursor.execute(sql)
    db.commit()

def deleteEdge(name1,name2):
    sql = 'delete from edge where name1 = \'%s\' and name2 = \'%s\'' %(name1,name2)
    cursor.execute(sql)
    sql = 'delete from edge where name1 = \'%s\' and name2 = \'%s\'' % (name2, name1)
    cursor.execute(sql)
    db.commit()

def getNodes():
    sql = 'select * from scenic_spot'
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getEdges():
    sql = 'select * from edge'
    cursor.execute(sql)
    return cursor.fetchall()

def carArrive(num,timeIn):
    if timeIn is None:
        sql = 'insert into Parking_log values(\'%s\',\'%s\',\'%s\',\'%s\')' \
              %(num,"0000-00-00 00:00:00","0000-00-00 00:00:00",0)
    else:
        sql = 'insert into Parking_log values(\'%s\',\'%s\',\'%s\',\'%s\')' % (num, timeIn, "0000-00-00 00:00:00",0)
    cursor.execute(sql)
    db.commit()


def carUpdateTimeIn(num,time):
    sql = 'update Parking_log set timeIn = \'%s\' where num = \'%s\' ' %(time,num)
    cursor.execute(sql)
    db.commit()

def carUpdateTimeOut(num,time):
    sql = 'update Parking_log set timeOut = \'%s\' where num = \'%s\' ' %(time,num)
    cursor.execute(sql)
    db.commit()

def carUpdateCost(num,cost):
    sql = 'update Parking_log set cost = \'%s\' where num = \'%s\' ' %(cost,num)
    cursor.execute(sql)
    db.commit()











