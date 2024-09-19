#   @Author: GitZamp
from collections import defaultdict
from os import rename,path,listdir,mkdir,name

#   Common file extensions.
audio = ('mp3', 'wav', 'midi')
video = ('mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'm4v', 'h264')
images = ('png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'svg',)
documents = ('txt', 'pdf', 'doc', 'docx', 'html', 'ppt', 'pptx', 'log')
compressed = ('zip', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb')
executables = ('dmg', 'exe', 'iso')


#   Main function that creates directories & maps files from downloads folder based on their file extensions.
def main():
    videofolder = "Videos"
    cwd = path.expanduser('~')
    if name == "nt":
        videofolder = "Movies"
    destindirs = ('Music', videofolder, 'Pictures', 'Documents', 'Applications', 'Other')
    for d in destindirs:
        dir_path = path.join(cwd, d)
        if not path.isdir(dir_path):
            mkdir(dir_path)
    # --------------------------------------------------------#
    downloads_path = path.join(cwd, 'Downloads')
    files_mapping = defaultdict(list)
    files_list = listdir(downloads_path)
    for file_name in files_list:
        if file_name[0] != '.':
            file_ext = file_name.split('.')[-1]
            files_mapping[file_ext].append(file_name)
    # --------------------------------------------------------#
    for f_ext, f_list in files_mapping.items():
        if f_ext in executables:
            for file in f_list:
                rename(path.join(downloads_path, file), path.join(cwd, 'Applications', file))
        elif f_ext in audio:
            for file in f_list:
                rename(path.join(downloads_path, file), path.join(cwd, 'Music', file))
        elif f_ext in video:
            for file in f_list:
                rename(path.join(downloads_path, file), path.join(cwd, videofolder, file))
        elif f_ext in images:
            for file in f_list:
                rename(path.join(downloads_path, file), path.join(cwd, 'Pictures', file))
        elif f_ext in documents or f_ext in compressed:
            for file in f_list:
                rename(path.join(downloads_path, file), path.join(cwd, 'Documents', file))
        else:
            for file in f_list:
                rename(path.join(downloads_path, file), path.join(cwd, 'Other', file))
