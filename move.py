import os
import shutil

folder_path = r'WHERE_YOUR_INVOICE_IS'

# 获取文件夹列表
folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

# 遍历文件夹并移动文件
for folder in folders:
    subfolder_path = os.path.join(folder_path, folder)
    files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
    
    for file in files:
        file_path = os.path.join(subfolder_path, file)
        destination_path = os.path.join(folder_path, file)
        shutil.move(file_path, destination_path)
    
    # 删除空文件夹
    os.rmdir(subfolder_path)
