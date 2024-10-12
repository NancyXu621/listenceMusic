import requests
import json
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 定义数据库模型
Base = declarative_base()

class Song(Base):
    __tablename__ = 'songs'
    
    id = Column(Integer, primary_key=True)
    song_id = Column(String, unique=True)
    details = Column(JSON)  # 存储JSON数据

# 创建数据库连接
engine = create_engine('sqlite:///songs.db')  # 使用SQLite数据库
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# 网易云音乐API接口示例 - 获取歌曲详情
url = "https://www.leborn.me/blog/home/page/0"
params = {
    "ids": "[123456]"  # 替换为实际的歌曲ID
}
headers = {
    "User-Agent": "Mozilla/5.0",
}

def fetch_song_details():
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def save_song_to_db(song_id, details):
    song = Song(song_id=song_id, details=details)
    session.add(song)
    session.commit()

def main():
    song_data = fetch_song_details()
    if song_data and 'songs' in song_data and song_data['songs']:
        for song in song_data['songs']:
            song_id = str(song['id'])
            save_song_to_db(song_id, song)  # 将数据存入数据库
            print(f"保存歌曲 ID: {song_id}")

if __name__ == "__main__":
    main()
