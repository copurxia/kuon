# pip install gitpython

from git.repo import Repo
import os
import shutil

# 获取当前地址文件地址
base_dir = os.path.dirname(os.path.abspath(__file__))
# 根目录
base_dir = os.path.dirname(base_dir)
# chatGPT目录
chatGPT_dir = os.path.join(base_dir,'chatGPT')
# 缓存文件夹
cache_dir = os.path.join(base_dir,'cache')

import stat
def readonly_handler(func, path, execinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

if __name__ == '__main__':
    # 判断目录是否存在
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)
    if not os.path.exists(chatGPT_dir):
        os.mkdir(chatGPT_dir)


    # 更新 https://github.com/acheong08/ChatGPT
    # 如果存在则删除
    acheong08ChatGPTPath = os.path.join(cache_dir,'acheong08ChatGPTPath')
    if os.path.exists(acheong08ChatGPTPath):
        shutil.rmtree(acheong08ChatGPTPath,onerror=readonly_handler)
    Repo.clone_from('https://github.com/acheong08/ChatGPT.git',to_path=acheong08ChatGPTPath,branch='main')
    # 将核心文件夹移动到chatGPT目录
    os.rename(os.path.join(acheong08ChatGPTPath,'src','revChatGPT'),os.path.join(chatGPT_dir,'revChatGPT'))
    #删除缓存文件夹及其内容
    shutil.rmtree(acheong08ChatGPTPath,onerror=readonly_handler)
    print('更新完成，该仓库消息请直接去 https://github.com/acheong08/ChatGPT 查看')

