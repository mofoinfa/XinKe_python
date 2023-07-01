class FileData:
    def __init__(self, filename):
        self.filename = filename
        try:
            f = open(self.filename, 'r', encoding='utf-8')
            self.file_list = eval(f.read())
            f.close()
        except FileNotFoundError:
            f = open(self.filename, 'w+', encoding='utf-8')
            f.write('[]')
            f.close()
            self.file_list = []

    def add_id(self, video_id):
        """数据的添加"""
        self.file_list.append(video_id)
        self.data_save()

    def select_id(self, video_id):
        """判断id是否存在"""
        if video_id in self.file_list:
            return True
        else:
            return False

    def data_save(self):
        """数据报错"""
        f = open(self.filename, 'w+', encoding='utf-8')
        f.write(str(self.file_list))
        f.close()

if __name__ == '__main__':
    FileData('data.txt')
