import logging
import connexion

# 禁用框架的log
logging.getLogger('connexion.middleware.main').disabled = True

# 当前服务器名称
app_name = 'user-manager'

application = connexion.FlaskApp(__name__, specification_dir="./swagger/")

# 需要用户登录才能访问的客户端接口
application.add_api(base_path='/api/project/usermanager/v1', specification='v1/user/user.json')

# # 服务器之间(微服务之间)请求的接口
# app.add_api(base_path='/api/projectsvc/usermanager/v1', specification='v1/service/user.json')

# # 需要admin角色才能访问的客户端接口
# app.add_api(base_path='/api/projectadm/usermanager/v1', specification='v1/admin/user.json')

# 不需要用户登录就能访问的客户端接口
application.add_api(base_path='/api/projectpub/usermanager/v1', specification='v1/public/account.json')
