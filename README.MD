### 一、接口文档

| 数据         | url                              | 参数                   | method |
| ------------ | -------------------------------- | ---------------------- | ------ |
| 获取全部图书 | http://127.0.0.1:5000/books      | /                      | GET    |
| 获取一本图书 | http://127.0.0.1:5000/books/{id} | id:number              | GET    |
| 新增一本图书 | http://127.0.0.1:5000/books      | data:object            | POST   |
| 修改一本图书 | http://127.0.0.1:5000/books/{id} | id:number，data:object | PUT    |
| 删除一本图书 | http://127.0.0.1:5000/books/{id} | id:number              | DELETE |

### 二、项目结构
book_erp
|--flask
|----app.py
|----App
|------__init__.py
|------apis.py	# api接口
|------config.py	# 数据库、跨域配置
|------exts.py
|------models.py
|------urls.py	# 路由
|--vue
|----src
|------main.ts
|------App.vue
|------request	# 封装axios
|--------http.ts	# 全局配置、拦截器配置
|--------api.ts	# api封装

### 三、配置项
#### flask
1、自建虚拟环境
2、更改配置项
config.py
    #db
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/bookerp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # cors
    ORIGINS = ["http://localhost:5173"]
    METHODS = ['GET','POST','PUT','DELETE']
### 四、启动项目
1、flask：运行app.py
2、vue
`npm run dev`
3、浏览器打开url：http:127.0.0.1:5173

### 五、后续开发
1、前后端的数据校验问题
2、搜索功能
3、分页功能