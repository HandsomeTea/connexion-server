import os
from flask import Response
from src.configs import HttpError, ErrorCode


def _stream_file_generator(file_path, chunk_size=1024 * 1024):
    """
    生成器：每次只读取 chunk_size 大小的数据。
    1024 * 1024 = 1MB，这是一个平衡了内存消耗和磁盘 IO 性能的经验值。
    """
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data


class Files:
    def download_file():
        # 前端下载操作:
        # window.open('http://localhost:8083/api/project/usermanager/v1/file/download');
        # 就是打开当前下载地址即可，最简单的下载方式，浏览器识别到这是文件下载，触发下载后会自动关闭空白标签

        # 同样兼容大文件下载，大文件下载前端操作：
        # import streamSaver from 'streamsaver';
        # const response = await fetch(url, ...);
        # const fileName = response.headers.get('Content-Disposition').split('filename=')[1];
        # response.body.pipeTo(streamSaver.createWriteStream(fileName))
        #   .then(() => console.log('下载完成'))
        #   .catch(err => console.error('传输中断:', err));
        path = "/home/SENSETIME/liuhaifeng/postman-linux-x64.tar.gz"

        if not os.path.exists(path):
            raise HttpError('File not found', ErrorCode.NOT_FOUND)

        # 封装成 Response
        response = Response(
            _stream_file_generator(path),
            mimetype='application/octet-stream'
        )
        # 强制浏览器弹出下载框，并告诉它文件名
        response.headers['Content-Disposition'] = f'attachment; filename={os.path.basename(path)}'

        # 告诉浏览器总长度，否则下载进度条会变成“无限循环”动画
        response.headers['Content-Length'] = os.path.getsize(path)

        return response
