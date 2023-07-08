import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

zip_folder = r'WHERE_YOUR_INVOICE_IS'
password_file = r'WHERE_YOUR_INVOICE_IS\password.txt'
seven_zip_path = r'C:\Program Files\7-Zip\7z.exe'
num_threads = 32

# 读取密码文件
with open(password_file, 'r') as file:
    passwords = [line.strip() for line in file]

# 定义解压函数
def extract_zip(zip_file):
    zip_file_path = os.path.join(zip_folder, zip_file)
    
    # 遍历密码列表
    for password in passwords:
        command = [seven_zip_path, 'x', '-p{}'.format(password), '-o{}'.format(zip_folder), zip_file_path, '-y']
        result = subprocess.run(command, capture_output=True)
        
        if result.returncode == 0:
            print('Extracted:', zip_file)
            return True
    
    print('Unable to extract:', zip_file)
    return False

# 使用线程池执行解压任务
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # 遍历ZIP文件夹中的所有ZIP文件
    zip_files = [file for file in os.listdir(zip_folder) if file.endswith('.zip')]
    results = executor.map(extract_zip, zip_files)

# 处理结果
for zip_file, result in zip(zip_files, results):
    if result:
        print('Successfully extracted:', zip_file)
    else:
        print('Failed to extract:', zip_file)
