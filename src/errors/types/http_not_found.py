class HttpNotFoundError(Exception):
    def __init__(self, message=str) -> None:
        self.message = message
        self.nome = "HtppNotFound"
        self.status_code = 404