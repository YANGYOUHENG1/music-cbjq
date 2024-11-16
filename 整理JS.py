import os
import json
from mutagen.mp3 import MP3

# 定义音乐文件夹和输出JSON文件的路径
music_dir = './music'
output_json = './music.json'

# 初始化一个列表来存储音乐文件的信息
music_files_info = []


# 定义一个函数来将时长转换为“分:秒”的格式
def format_duration(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes}:{seconds:02}"


# 遍历音乐文件夹中的所有文件
for filename in os.listdir(music_dir):
    if filename.endswith('.mp3'):
        # 获取文件的完整路径
        file_path = os.path.join(music_dir, filename)

        # 使用mutagen读取MP3文件的时长
        audio = MP3(file_path)
        duration = format_duration(audio.info.length)

        # 根据文件名设置封面图片路径
        cover = "./picture/尘白.png"
        if '1.1' in filename:
            cover = "./picture/1.1.png"
        elif '1.2' in filename:
            cover = "./picture/1.2.png"
        elif '1.3' in filename:
            cover = "./picture/1.3.png"
        elif '1.4' in filename:
            cover = "./picture/1.4.png"
        elif '1.5' in filename:
            cover = "./picture/1.5.png"
        elif '1.6' in filename:
            cover = "./picture/1.6.png"
        elif '1.7' in filename:
            cover = "./picture/1.7.png"
        elif '1.8' in filename:
            cover = "./picture/1.8.png"
        elif '2.0' in filename:
            cover = "./picture/2.0.png"
        elif '2.1' in filename:
            cover = "./picture/2.1.png"
        elif '2.2' in filename or '2.3' in filename:
            cover = "./picture/2.3.png"

        # 将文件名中的“.mp3”字样移除
        clean_filename = filename.replace('.mp3', '')

        # 将文件名和时长信息存储到字典中
        music_info = {
            "name": clean_filename,
            "audio_url": os.path.join(music_dir, filename).replace('\\', '/'),
            "singer": "尘白禁区",
            "album": "西山居",
            "cover": cover.replace('\\', '/'),
            "time": duration
        }

        # 将字典添加到列表中
        music_files_info.append(music_info)

# 将列表写入JSON文件
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(music_files_info, f, ensure_ascii=False, indent=4)

print(f"音乐文件信息已写入 {output_json}")
