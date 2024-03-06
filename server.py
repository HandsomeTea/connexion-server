import src.middlewares  # noqa: F401
from app import application
from src.configs import log_config, get_env


__run_config__ = {
    'port': 8083,
    'log_config': log_config,
    'access_log': False
}

if (get_env('ENV') == 'development'):
    __run_config__.update({
        # 修改代码保存重启的配置，server为当前文件名，application为app的变量名(app.py抛出的application)
        'import_string': 'server:application',
        'reload': True,
    })

if __name__ == '__main__':
    application.run(**__run_config__)
