import shutil
import os
import glob
import sys


def appender(list_res, list_dest):
    if len(list_res) != 0:
        for i in list_res:
            list_dest.append(i)


def mover(list_res, dest_path):
    if len(list_res) != 0:
        for i in list_res:
            shutil.move(i, dest_path)

def clean():
    home = os.path.expanduser('~')
    if sys.platform == 'linux':
        home_downl = home + '/Загрузки'
        path_to_distr = home + '/Загрузки/Files'
    else:
        home_downl = home + 'Downloads'
        path_to_distr = r'=F:/Distr'

    print(home_downl)
    print("Сбор данных...")
    list_of_images = glob.glob(home_downl + '/*.jpeg')
    list_of_png = (glob.glob(home_downl + '/*.png'))
    list_of_jpg = (glob.glob(home_downl + '/*.jpg'))
    appender(list_of_jpg, list_of_images)
    appender(list_of_png, list_of_images)

    list_of_video = glob.glob(home_downl + '/*.webm')
    list_of_mp4 = glob.glob(home_downl + '/*.mp4')
    appender(list_of_mp4, list_of_video)

    list_of_music = glob.glob(home_downl + '/*.mp3')
    list_of_docs = glob.glob(home_downl + '/*.pdf')
    list_of_torr = glob.glob(home_downl + '/*.torrents')
    list_of_exe = glob.glob(home_downl + '/*.exe')
    list_of_arch = glob.glob(home_downl + '/*.zip')
    list_of_tar = glob.glob(home_downl + '/*.tar.*')
    appender(list_of_tar, list_of_arch)

    print('Количество файлов "Images: %s"\n'
          'Количество файлов "Video: %s"\n'
          'Количество файлов "Music: %s"\n'
          'Количество файлов "Torrents: %s"\n'
          'Количество файлов "Exe: %s"\n'
          'Количество файлов "Docs: %s"\n'
          'Количество файлов "Zip: %s"\n' %
          (len(list_of_images),
           len(list_of_video),
           len(list_of_music),
           len(list_of_torr),
           len(list_of_exe),
           len(list_of_docs),
           len(list_of_arch)))

    mover(list_of_images, os.path.join(home, '/Изображения'))
    mover(list_of_video, os.path.join(home, '/Видео'))
    mover(list_of_music, os.path.join(home, '/Музыка'))
    mover(list_of_arch, path_to_distr)
    mover(list_of_exe, path_to_distr)
    mover(list_of_docs, os.path.join(home, '/Документы'))
    mover(list_of_torr, os.path.join(home, '/torrents'))


if __name__ == '__main__':
    print("Начало очистки папки...")
    clean()
