from .exts import api
from .apis import BookResource,BooklistResource

api.add_resource(BookResource,'/books/<int:bid>')
api.add_resource(BooklistResource,'/books')