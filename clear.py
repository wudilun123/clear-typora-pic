import os
from send2trash import send2trash

pic_dir = r'***'  #本地图片目录路径
md_path = r'***' #md文件路径
useless_pic_path_list = []

for root, dirs, files in os.walk(pic_dir):
    try:
        with open(md_path, 'r', encoding='utf-8') as fp:
            md_text = fp.read()
            # print(md_text)
            for file in files:
                if md_text.find(file) == -1:
                    useless_pic_path_list.append(os.path.join(root, file))
                # print(file)
    except Exception as e:
        print(e)
    break

print('未引用文件如下:')
print(useless_pic_path_list)
flag = input('要删除以上文件吗?(y/n)')
if flag == 'y':
    for pic_path in useless_pic_path_list:
        try:
            # os.remove(pic_path)
            send2trash(pic_path)
            print('已删除未引用文件:%s' % pic_path)
        except Exception as e:
            print('删除未引用文件失败:%s' % pic_path)
