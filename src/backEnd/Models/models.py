class Responses:
    Response:object
    Error:bool

    def generaRespuestaGenerica(self, response, error=False):
        self.Response =response
        self.Error =error