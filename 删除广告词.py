# 该脚本目的是为了删除广告词
import os

folder_path = '存放.txt文件的文件夹路径'  # 存放 TXT 文件的文件夹路径
target_texts = ['你要删除的文字，可批量']

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        new_content = original_content
        for target_text in target_texts:
            new_content = new_content.replace(target_text, '')
        if new_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
