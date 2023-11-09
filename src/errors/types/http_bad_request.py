class HttpBadRequestError(Exception):
    def __init__(self, message:str) -> None:
        self.message = message
        self.nome = "BadRequest"
        self.status_code = 400


