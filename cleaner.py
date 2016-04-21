import sys
import shutil
import mimetypes
import os
from logging import shutdown


def clean():
    home = os.path.expanduser('~')
    print(home)
    print("Сбор данных...")
    path_j = os.getcwd()
    list_of_files = os.listdir(os.path.join(home, r'Downloads'))
    list_of_images = []
    list_of_video = []
    list_of_music = []
    list_of_docs = []


    for i in list_of_files:
        if i.lower().endswith('.jpg') | i.lower().endswith('.jpeg') |\
                i.lower().endswith('.png') | i.lower().endswith('.gif'):
            list_of_images.append(i)
        elif i.lower().endswith('.webm') | i.lower().endswith('.mp4'):
            list_of_video.append(i)
        elif i.lower().endswith('.mp3'):
            list_of_music.append(i)
        elif i.lower().endswith('.pdf'):
            list_of_docs.append(i)

    print('Количество файлов "Images: %s"\n'
          'Количество файлов "Video: %s"\n'
          'Количество файлов "Music: %s"\n'
          'Количество файлов "Docs: %s"\n' %
          (len(list_of_images), len(list_of_video), len(list_of_music), len(list_of_docs)))

    for i in list_of_images:
        shutil.move(os.path.join(os.path.join(home, 'Downloads'), i), os.path.join(home, 'Pictures'))

    for i in list_of_music:
        shutil.move(os.path.join(os.path.join(home, 'Downloads'), i), os.path.join(home, 'Music'))

    for i in list_of_docs:
        shutil.move(os.path.join(os.path.join(home, 'Downloads'), i), os.path.join(home, 'Documents'))

    for i in list_of_video:
        shutil.move(os.path.join(os.path.join(home, 'Downloads'), i), os.path.join(home, 'Videos'))
if __name__ == '__main__':
    print("Начало очистки папки...")
    clean()
