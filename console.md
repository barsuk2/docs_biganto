
### biganto.com-help
#### работа в консоле🤩️
Простые ORM запросы не работают. Нужно создавать контекст приложения

https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

from visual.app import create_app
app= create_app('config.local.py')
app.app_context().push()
from visual.core import db
from visual.models import Tour, Footage


### bogenhouse
from bogenhouse.app import create_app
app= create_app('config.local.py')
app.app_context().push()
from bogenhouse.core import db
from bogenhouse.models.estates import Estate
Estate.query.all()


### room-park
from roompark.app import create_app
app= create_app('config.local.py')
app.app_context().push()
from roompark.core import db
from roompark.models.estates import Estate

Estate.query.all()
from bogenhouse.models.documents import Document
from bogenhouse import create_app

app = create_app('config.local.py')

with app.app_context():
    Document.query.all()



