class APIConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.base_url = "https://jsonplaceholder.typicode.com"
        return cls._instance