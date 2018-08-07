#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/xuemc_db',echo=True)
#DBsession = sessionmaker(bind = engine)
#session = DBsession()
#query = session.execute('select * from student')
#query = query.fetchall()
#print(query)

#orm方式
#from sqlalchemy import Column,String,create_engine
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base

#db = declarative_base()

#class Stu(db):
#    __tablename__ = 'STUDENT'
#    SNO = Column(String(7),primary_key=True)
#    SNAME = Column(String(8))
#    SEX = Column(String(2))

#engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/xuemc_db',echo=True)
#DBsession = sessionmaker(bind=engine)
#session = DBsession()
#new_stu=Stu(SNO='9302205',SNAME='方邪真',SEX='男') 
#session.add(new_stu)
#session.commit()
#query = session.query(Stu)
#session.close()


