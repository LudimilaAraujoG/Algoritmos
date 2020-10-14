
class FIFO:
    """TRABALHO DE SISTEMAS OPERACIONAIS ABERTOS"""

    def execute(self, quad_vlr, referencias):
        pag_falta_mem = 0 
        mem = [] 
    
        for ref in referencias:
            if ref not in mem:
                pag_falta_mem += 1 
                
                if len(mem) == quad_vlr:
                    mem.pop(0)
              
                mem.append(ref)

        return pag_falta_mem
