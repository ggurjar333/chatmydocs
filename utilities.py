import pathlib


class Utility:

    def __init__(self):
        self._name = ""

    def create_tmp_folder(self, folder_name):
        self._name = folder_name
        p = pathlib.Path(self._name)
        p.mkdir(parents=True, exist_ok=True)
        # return print(f'{p} folder created.')

    def __str__(self) -> str:
        return str(self._name)

# if __name__=="__main__":
#     ut = Utility()
#     ut.create_tmp_folder(folder_name='tmp')
#     print(str(ut))