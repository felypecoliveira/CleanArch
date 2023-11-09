class HttpUnprocessableEntityError(Exception):
    def __init__(self, message=str) -> None:
        self.message = message
        self.nome = "HttpUnprocessableEntity"
        self.status_code = 422