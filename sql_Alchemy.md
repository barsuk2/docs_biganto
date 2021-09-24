### VERSION
sqlalchemy.__version__
flask_sqlalchemy.__version__



### ORDER_BY

1 Accessing the field properties asc and dsc:
query.order_by(SpreadsheetCells.y_index.desc()) # desc
query.order_by(SpreadsheetCells.y_index.asc()) # asc

2 Using the asc and desc module functions:

from sqlalchemy import asc, desc

query.order_by(desc(SpreadsheetCells.y_index)) # desc
query.order_by(asc(SpreadsheetCells.y_index)) # asc

### FILTER

session.query(User).filter(User.name == 'Bob')
session.query(User).filter(User.birthday < dt.date(2000, 1, 1))
For the first case, there is a shortcut:

session.query(User).filter_by(name='Bob')

### LIMIT

User.query.limit(1).all()

User.query.filter(User.email.endswith('@example.com')).all() - отфильтовать окнанчиватеся на example.com

Конструкция LIKE
Tour.query.filter(Tour.title.like('Empty%')).first()


Конструкция IN Вхождение
Tour.query.filter(Tour.footage_id.in_([1,2])

Конструкция ИЛИ Вхождение
result = session.query(Customers).filter(or_(Customers.id>2, Customers.name.like('Ra%'))))


Связь один ко многим удобно реализовывать через систему парных ссылок в моделях. 


JION

user = User.query.get(5).join(TeamMember).outerjoin(TeamMemberStatus, TeamMemberStatus.finish > datatime.datatime.now() )
user = db.session.query(User).join(TeamMember).outerjoin(TeamMemberStatus, TeamMemberStatus.finish > datatime.datatime.now() )

ery = db.session.query(User, TeamMemberStatus, TeamMember).join(TeamMember).outerjoin(TeamMemberStatus)


### DISTINCT - отоборать уникальные

db.session.query(User.created_by).distinct().all()

### array_agg

q = db.session.query(User, db.func.array_agg(TeamMemberStatus.id)).join(TeamMember).outerjoin(TeamMemberStatus).group_by(User.id)


q = db.session.query(User,db.func.array_agg(TeamMemberStatus.type)).join(TeamMember).outerjoin(TeamMemberStatus).group_by(User.id)



q = db.session.query(User, cast(db.func.array_agg(db.func.row(TeamMemberStatus.type,'||',TeamMemberStatus.start,'||',TeamMemberStatus.finish)),ARRAY(String))).join(TeamMember).outerjoin(TeamMemberStatus).group_by(User.id)



q = db.session.query(User, db.func.row(db.func.array_agg(TeamMemberStatus.type),db.func.array_agg(TeamMemberStatus.start))).join(TeamMember).outerjoin(TeamMemberStatus).group_by(User.id)


q = db.session.query(User, db.func.array_agg(TeamMemberStatus.query.all())).join(TeamMember).outerjoin(TeamMemberStatus).group_by(User.id)
#### Вложенные запросы

Вывести имена пользователей, членов команды	

sub = db.session.query(TeamMember.user_id).subquery()

Вывести имена из 1 отдела
dep = db.session.query(TeamMember.user_id,TeamMember.department_id).filter(TeamMember.department_id == 1).subquery('sub')
q= db.session.query(User.name, dep.c.department_id).join(dep, User.id == dep.c.user_id) 

print(sub.c) - посмотреть таблицу




[(<User 9:Строкина Татьяна>, '("{4,5,8,9}","{2019-08-01,2020-08-01,2021-09-01,2022-08-01}","{2019-08-01,2020-08-01,2021-09-01,2022-08-01}")'), (<User 42:kasiatora>, '("{6,7}","{2021-08-01,2019-08-01}","{2021-08-01,2019-08-01}")'), (<User 4:NEWBIE@BIGANTO.COM>, '({NULL},{NULL},{NULL})'), (<User 50:Новый>, '({NULL},{NULL},{NULL})'), (<User 49:qqq>, '({NULL},{NULL},{NULL})'), (<User 40:werwt>, '({NULL},{NULL},{NULL})'), (<User 48:egor ццц>, '({NULL},{NULL},{NULL})'), (<User 47:egor>, '({NULL},{NULL},{NULL})'), (<User 32:eweq123123>, '({NULL},{NULL},{NULL})')]


[(<User 9:Строкина Татьяна>, ['(sick-leave,2019-08-01,2019-08-24)', '(maternity-leave,2020-08-01,2020-08-24)', '(vacation,2021-09-01,2021-09-24)', '(vacation,2022-08-01,2022-08-24)']), (<User 42:kasiatora>, ['(vacation,2021-08-01,2021-08-24)', '(vacation,2019-08-01,2019-08-24)']), (<User 4:NEWBIE@BIGANTO.COM>, ['(,,)']), (<User 50:Новый>, ['(,,)']), (<User 49:qqq>, ['(,,)']), (<User 40:werwt>, ['(,,)']), (<User 48:egor ццц>, ['(,,)']), (<User 47:egor>, ['(,,)']), (<User 32:eweq123123>, ['(,,)'])]


