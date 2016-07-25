import shutil
import os


def clean():
    home = os.path.expanduser('~')
    path_to_distr = r'F:\Distrib'
    print(home)
    print("Сбор данных...")
    list_of_files = os.listdir(os.path.join(home, r'Downloads'))
    list_of_images = []
    list_of_video = []
    list_of_music = []
    list_of_docs = []
    list_of_torr = []
    list_of_exe = []

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
        elif i.lower().endswith('.exe'):
            list_of_exe.append(i)
        elif i.lower().endswith('.torrent'):
            list_of_torr.append(i)

    print('Количество файлов "Images: %s"\n'
          'Количество файлов "Video: %s"\n'
          'Количество файлов "Music: %s"\n'
          'Количество файлов "Torrents: %s"\n'
          'Количество файлов "Exe: %s"\n'
          'Количество файлов "Docs: %s"\n' %
          (len(list_of_images),
           len(list_of_video),
           len(list_of_music),
           len(list_of_torr),
           len(list_of_exe),
           len(list_of_docs)))

    for i in list_of_images:
        shutil.move(os.path.join(os.path.join(home, 'Downloads'), i), os.path.join(home, 'Pictures'))

    for i in list_of_music:
        shutil.move(os.path.join(os.path.join(home, 'Downloads'), i), os.path.join(home, 'Music'))

    for i in list_of_docs:
        shutil.move(os.path.join(os.path.join(home, 'Downloads'), i), os.path.join(home, 'Documents'))

    for i in list_of_video:
        shutil.move(os.path.join(os.path.join(home, 'Downloads'), i), os.path.join(home, 'Videos'))

    for i in list_of_torr:
        shutil.move(os.path.join(os.path.join(home), 'Downloads'), i),\
                    os.path.join(home, os.path.join('Downloads', 'torr'))
    for i in list_of_exe:
        try:
            shutil.move(os.path.join(os.path.join(home, 'Downloads'), i), path_to_distr)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print("Начало очистки папки...")
    clean()
