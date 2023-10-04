import pathlib


class Utility:

    def __init__(self):
        self._file_name = None
        self._name = None

    def create_tmp_folder(self, folder_name):
        self._name = folder_name
        p = pathlib.Path(self._name)
        p.mkdir(parents=True, exist_ok=True)
        # if not pathlib.Path(self._name):
            # return pathlib.Path(self._name).mkdir(parents=True, exist_ok=True)

    def delete_tmp_folder(self, folder_name, file_name):
        self._name = folder_name
        self._file_name = file_name
        rem_file = pathlib.Path(f'{self._name}' + '/'+{self._file_name})
        rem_file.unlink()
        rem_folder = pathlib.Path(self._name)
        rem_folder.rmdir()

    def __str__(self) -> str:
        return str(self._name)
