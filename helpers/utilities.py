import pathlib


class Utility:

    def __init__(self):
        self._name = ""

    def create_tmp_folder(self, folder_name):
        self._name = folder_name
        p = pathlib.Path(self._name)
        p.mkdir(parents=True, exist_ok=True)
        # if not pathlib.Path(self._name):
            # return pathlib.Path(self._name).mkdir(parents=True, exist_ok=True)

    def __str__(self) -> str:
        return str(self._name)
