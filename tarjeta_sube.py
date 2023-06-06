class NoHaySaldoException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass

PRIMARIO = 'primario' 
SECUNDARIO = 'secundario'
UNIVERSITARIO = 'universitario'
JUBILADO = 'jubilado'

PRECIO_TICKET = 70
DESACTIVADO ='desactivado'
ACTIVADO = 'activado'

DESCUENTOS = {
    PRIMARIO: 0.5,
    SECUNDARIO: 0.4,
    UNIVERSITARIO: 0.3,
    JUBILADO: 0.25,
}

class Sube:
    def __init__(self):
        self.saldo = 1000
        self.grupo_beneficiario = None
        self.estado = ACTIVADO
    
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == PRIMARIO:
            precio_ticket = PRECIO_TICKET - DESCUENTOS[PRIMARIO] * PRECIO_TICKET
        elif self.grupo_beneficiario == SECUNDARIO:
            precio_ticket = PRECIO_TICKET - DESCUENTOS[SECUNDARIO] * PRECIO_TICKET
        else:
            precio_ticket = PRECIO_TICKET
        return precio_ticket
    
    def pagar_pasaje(self):
        if self.saldo < self.obtener_precio_ticket():
            raise NoHaySaldoException
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException
        self.saldo -= self.obtener_precio_ticket()

    def cambiar_estado(self,estado):
        if estado == ACTIVADO:
            self.estado = estado
        elif estado ==  DESACTIVADO:
            self.estado = estado
        else:
            raise EstadoNoExistenteException
        
