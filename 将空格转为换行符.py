# 该脚本目的是为了美化观看体验
import os

input_folder = '输入文件夹路径'  # 输入文件夹路径
output_folder = '输出文件夹路径'  # 输出文件夹路径

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)
        with open(input_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = content.replace('　　', '\n')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
