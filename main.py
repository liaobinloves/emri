import numpy as np
import constant as cons
import matplotlib.pyplot as plt


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
        self.kind = kind

    def __setattr__(self, name, value):
        if name == 'kind':
            self.par = Parameter()(value)
        super().__setattr__(name, value)

    def __call__(self, energy):
        tmp = energy < 0
        return np.append(self.lhs(energy[tmp]), self.rhs(energy[~tmp]))

    def lhs(self, energy):
        n_star = 2.8e5/self.cons.pc**3
        sigma = 1.03e7
        return n_star/(2*np.pi*sigma**2)**1.5*(-energy/sigma**2)**self.par['pm']

    def rhs(self, energy):
        sigma = 1.03e7
        n_star = 2.8e5/self.cons.pc**3
        return n_star/(2*np.pi*sigma**2)**1.5*np.exp(-energy/sigma**2)

def cal_energy(e, rp):
    c = cons.Constant
    return -(1-e)*c.G*c.Mmilky/rp/2.

def main():
    df = DF()
    c = cons.Constant
    # x = np.linspace(-10000, 10000, 256)
    # y = df(x)

    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # plt.show()

    print(df(np.array([cal_energy(0.5, 1e-1*1.7*c.pc)])))


if __name__ == '__main__':
    main()