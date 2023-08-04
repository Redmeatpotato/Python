import os
import shutil

def convert_backslashes_to_slashes(path):
    return path.replace("\\", "/")

folder_path = r'C:\Users\ChenJ\Desktop\任务2023.8.2\20230323给排水-已盖章\17、第三册 给排水 第十七分册 变配电房'  # 修改为你的文件夹路径
converted_path = convert_backslashes_to_slashes(folder_path)

# 使用os模块获取文件夹中的所有文件名
file_names = os.listdir(converted_path)

# 使用sorted函数对文件名进行排序
sorted_file_names = sorted(file_names)

print(sorted_file_names)
