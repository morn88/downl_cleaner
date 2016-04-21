import sys
import shutil
import mimetypes
import os
from logging import shutdown


def clean():
    print("Сбор данных...")
    path_j = os.getcwd()
    list_of_files = os.listdir(r'C:\Users\ЭМПРиО\Downloads')
    list_of_images = []
    list_of_video = []
    list_of_music = []
    list_of_docs = []


    for i in list_of_files:
        if i.endswith('.jpg') | i.endswith('.jpeg') | i.endswith('png'):
            list_of_images.append(i)
        elif i.endswith('.webm'):
            list_of_video.append(i)
        elif i.endswith('.mp3'):
            list_of_music.append(i)
        elif i.endswith('.pdf'):
            list_of_docs.append(i)

    print('Количество файлов "Images: %s"\n'
          'Количество файлов "Video: %s"\n'
          'Количество файлов "Music: %s"\n'
          'Количество файлов "Docs: %s"\n' %
          (len(list_of_images), len(list_of_video), len(list_of_music), len(list_of_docs)))

    for i in list_of_images:
        shutil.move(os.path.join(r'C:\Users\ЭМПРиО\Downloads', i), r'C:\Users\ЭМПРиО\Pictures')

if __name__ == '__main__':
    print("Начало очистки папки...")
    clean()
