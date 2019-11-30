import numpy as np
import constant as cons


class Parameter:
    def __init__(self):
        self.kind = ('MS', 'WD', 'NS', 'BH')
        pm = (-0.1, -0.1, 0., 0.5)
        
        self.par = {'kind':self.kind, 'pm':pm}

    def __call__(self, kind):
        idx = self.kind.index(kind)
        res = dict()
        for i in self.par:
            res[i] = self.par[i][idx]
        return res

class DF:
    def __init__(self, kind='MS'):
        self.cons = cons.Constant
        self.par = Parameter()(kind)


#     def func_left(self, e):
#         return (-e)

    def __call__(self, e):
        return self.par

def main():
    df = DF('BH')
    print(df(10))

if __name__ == '__main__':
    main()