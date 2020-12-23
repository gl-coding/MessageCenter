# 导入:
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Float, Integer, String, MetaData, ForeignKey
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Users(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    email = Column(String(64))

    def __init__(self, name, email):
        self.name = name
        self.email = email

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/aa')
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))

# 生成数据库表
Base.metadata.create_all(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()
add_user = Users("test", "test123@qq.com")
session.add(add_user)
session.commit()

users = session.query(Users).filter_by(id=1).all()
for item in users:
    print(item.name)

session.query(Users).filter_by(id=1).update({'name': "Jack"})

users = session.query(Users).filter_by(id=1).all()
for item in users:
    print(item.name)

session.query(Users).filter(Users.name == "test").delete()
session.commit()

#利用基类删除所有的数据库表
Base.metadata.drop_all(engine)