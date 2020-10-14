
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class LRU:
    """TRABALHO SISTEMAS OPERACIONAIS ABERTOS"""

    def execute(self, qtd_quadros, referencias):
        
        pag_falta_mem = 0 
        inicio = 0
        mem = {} 

        for ref in referencias:
            if ref not in mem.keys():
                pag_falta_mem += 1 

                
                if len(mem) == qtd_quadros:
                    ant = self.paginaAntiga(mem)
                    del mem[ant] 
   
            mem[ref] = inicio
            inicio += 1

        
        return pag_falta_mem


    def paginaAntiga(self, mem):

    
        ant = mem.keys()[0]
        maisRapido = mem.values()[0]
      
        for ch in mem.keys():
            
            if mem[ch] < maisRapido:
                ant = ch
                maisRapido = mem[ch]

        return ant
