import pymysql

#db=pymysql.connect('hostname','username','password')
#db=pymysql.connect('we1sfxmpdkinhpy-c.cluster-ceas0akte0b1.eu-west-1.rds.amazonaws.com','digitalassets','')
#db=pymysql.connect('digitalassets-db-cluster.cluster-cttz2jcetxsj.eu-west-1.rds.amazonaws.com','-sysop-kun6bk-w@bp365.onmicrosoft.com','g.j8.RWEzncB6bQ$')

db1 = pymysql.connect(
  host="we1sfxmpdkinhpy-c.cluster-ceas0akte0b1.eu-west-1.rds.amazonaws.com",
  user="digitalassets",
  password="C#Q7tWmSSVCBX8D"
)



print(db1)
cursor=db1.cursor()
cursor.execute("use SDA_RMA_DE;")
cursor.execute("select * from tasks limit 10;")
data= cursor.fetchall()
print(data)
