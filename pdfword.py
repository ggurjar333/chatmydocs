import pathlib
from llama_index import SimpleDirectoryReader, VectorStoreIndex
from utilities import Utility


class PdfWord:
    def __init__(self):
        self._folder_name = ""
        self._prompt = ""

    def analyze(self, temp_dir, user_prompt_text):
        self._folder_name = temp_dir
        self._prompt = user_prompt_text

        # Create a temp directory
        ut = Utility()
        ut.create_tmp_folder(folder_name=self._folder_name)

        documents = SimpleDirectoryReader(self._folder_name).load_data()
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()
        response = query_engine.query(
            "You're an intelligent subject expert and humorist, Respond the following query the data "
            + self._prompt)
        print(response)
        return str(response)


if __name__ == "__main__":
    pw = PdfWord()
    pw.analyze(temp_dir='')