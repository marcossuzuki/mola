from math import pi

class Mola:

    def __init__(self, d_arame=None, d_medio=None, d_int=None, d_ext=None, tipo=None):
        self.__d = {}
        diametro_exist = self.__calc_diametro(arame=d_arame, medio=d_medio, int=d_int, ext=d_ext)
        self.tipo = tipo
        if diametro_exist is not None:
            self.__calc_forma()

    def __calc_diametro(self, **kwargs):
        not_none = 0
        for k, val in kwargs.items():
            if val != None:
                not_none += 1
                self.__d[k] = val
                print(k, self.__d[k])
        if not_none < 2:
            print('Não é possível realizar o calculo')
            return None 
        

    def __calc_forma(self):
        self.__w = self.w
        self.__ks = self.ks
        self.__kw = self.kw
        self.__kb = self.kb
        self.__kc = self.kc
    
    @property
    def d_arame(self): 
        return self.__d['arame']
    
    @d_arame.setter
    def d_arame(self, value):
        self.__d['arame'] = value
        self.__calc_forma()

    @property
    def d_medio(self): 
        return self.__d['medio']
    
    @d_medio.setter
    def d_medio(self, value):
        self.__d['medio'] = value
        self.__calc_forma()

    @property
    def d_int(self): 
        return self.__d['int']
    
    @d_int.setter
    def d_int(self, value):
        self.__d['int'] = value
        self.d_medio = self.d_int + self.d_arame
        self.__calc_forma()
    
    @property
    def d_ext(self): 
        return self.__d['ext']

    @property
    def w(self): 
        return self.d_medio/self.d_arame
       
    @property
    def ks(self):
        w = self.__w
        ks = (2*w+1)/(2*w)
        return ks
    
    @property
    def kw(self):
        w = self.__w
        kw = (4*w-1)/(4*w-4)+0.615/w
        return kw

    @property
    def kb(self):
        w = self.__w
        kb = (4*w+2)/(4*w-3)
        return kb
    
    @property
    def kc(self): 
        return self.__kb/self.__ks

    def calc_tensao(self, force:float):
        d_medio = self.d_medio
        d_arame = self.d_arame
        return self.kb*(8*force*d_medio)/(pi*d_arame**3)

    # def __str__(self):
    #     return self.__name__


if __name__ == '__main__':
    mola = Mola( d_medio=.4)
    # print(mola.calc_tensao(force=6.46))
    # print(f'Indice da mola: {mola.w}')
    # print(f'Kb: {mola.kb}')
    # print(f'Kc: {mola.kc}')
    # print(f'Ks: {mola.ks}')
    # print(f'Kw: {mola.kw}')
    # mola.d_arame = 0.04
    # print(mola.d_arame)
    # print(mola.calc_tensao(force=6.46))
    # print(f'Indice da mola: {mola.w}')
    # print(f'Kb: {mola.kb}')
    # print(f'Kc: {mola.kc}')
    # print(f'Ks: {mola.ks}')
    # print(f'Kw: {mola.kw}')
    mola2 = Mola(0.04, 0.8)
    # print(mola2.d_ext)
    # print(mola2.d_int)
    # print(mola2.d_medio)
