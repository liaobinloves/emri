import numpy as np
from astropy import constants as c
from astropy import units as u
import matplotlib.pyplot as plt
import sub


class Parameter:
    def __init__(self):
        self.kind = ('MS', 'WD', 'NS', 'BH', 'single')
        pm = (-0.1, -0.1, 0., 0.5, 0.25)
        
        self.par = {'kind':self.kind, 'pm':pm}

    def __call__(self, kind):
        idx = self.kind.index(kind)
        res = dict()
        for i in self.par:
            res[i] = self.par[i][idx]
        return res

class DF:
    sigma = 103 * u.km/u.s
    M_g = 4.31e6 * c.M_sun
    m_star = 6.4e6 * c.M_sun
    rc = c.G*M_g/sigma**2
    n_star = 3.*m_star/(4.*np.pi*rc**3*c.M_sun)

    constant = n_star/(2.*np.pi*sigma**2)**1.5

    def __init__(self, kind='MS'):
        self.kind = kind

    def __setattr__(self, name, value):
        if name == 'kind':
            self.par = Parameter()(value)
        super().__setattr__(name, value)

    def __call__(self, energy):
        tmp = energy < 0
        return np.append(self.lhs(energy[tmp]), self.rhs(energy[~tmp]))

    def _ms_rtde(self):
        return 7e12*(self.M_g/(1e6*c.M_sun))**(1./3)*u.cm

    def _wd_rtde(self):
        return

    @property
    def rtde(self):
        if self.kind == 'MS':
            return self._ms_rtde()
        elif self.kind == 'WD':
            return self._wd_rtde()

    def lhs(self, energy):
        n_star = 2.8e5/c.pc**3
        sigma = 1.03e7
        return 2*n_star/(2*np.pi*sigma**2)**1.5*(-energy/sigma**2)**self.par['pm']

    def rhs(self, energy):
        sigma = 1.03e7
        n_star = 2.8e5/c.pc**3
        return n_star/(2*np.pi*sigma**2)**1.5*np.exp(-energy/sigma**2)

    def cal_energy(self, e, rp):
        return -(1-e)*c.G*self.M_g/rp/2.

def main():
    # df = DF('MS')
    # print(df.par)
    # c = c.Constant
    # x = np.linspace(-10000, 10000, 256)
    # y = df(x)

    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # plt.show()

    # print(df(np.array([cal_energy(0.5, 1e-1*1.7*c.pc)])))

    # mass1 = 4.31e6
    # mass2 = 4.31e5
    # x1, y1 = sub.cal_coll_cut(mass1)
    # x2, y2 = sub.cal_coll_cut(mass2)
    # fig, ax = plt.subplots()
    # ax.set_xlabel('e')
    # ax.set_ylabel('log10(rp/rc)')
    # ax.plot(x1, y1, c='r')
    # ax.plot(x2, y2, c='b')
    # plt.savefig('rp_rc.png')

    t = DF()
    print(t.rtde)
    print(4.31**(1./3)*7e12)


if __name__ == '__main__':
    main()