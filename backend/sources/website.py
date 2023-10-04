from llama_index import download_loader, VectorStoreIndex


class Website:

    def __init__(self):
        self._url = ""
        self._prompt = ""

    def analyze(self, user_website_link, user_prompt_text):
        self._url = user_website_link
        self._prompt = user_prompt_text

        BeautifulSoupWebReader = download_loader("BeautifulSoupWebReader")
        loader = BeautifulSoupWebReader()
        documents = loader.load_data(urls=[self._url])
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()
        response = query_engine.query(
            "As intelligent website recruiting AI chatbot, Respond to the following query." + self._prompt)
        return str(response)

    def __str__(self) -> dict:
        return str(self._url, self._prompt)
