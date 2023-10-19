class IndOriented(Individuo):
    def __init__(self, x, eq, land=None):
        super().__init__(x, eq, land=land)
        self.percep = self.hrs / 2
        self.land= land

    def move(self):
        ponto = Point(self.coord[-1][0], self.coord[-1][1])
        buff = ponto.buffer(self.percep)
        rec, recorte = mask(self.land, [buff], crop=False)
        c_hab = np.where(rec[0, :, :] == 1)
        c_nhab= np.where(rec[0,:,:]==0)
        sc_hab = len(c_hab[0])

        if sc_hab >= 1:
            esc = rd.choice(range(sc_hab))
            escoord = convert(c_hab[0][esc], c_hab[1][esc], recorte)
            self.coord.append([escoord[0], escoord[1]])
            
        elif len(c_nhab[0]):
            esc = rd.choice(range(len(c_nhab[0])))
            escoord = convert(c_nhab[0][esc], c_nhab[1][esc], recorte)
            self.coord.append([escoord[0], escoord[1]])
            
        else:
          teta = np.random.uniform(size=1) * 2 * np.pi
          xcoord = self.coord[-1][0] + self.hrs * np.cos(teta)
          ycoord = self.coord[-1][1] + self.hrs * np.sin(teta)
          self.coord.append([xcoord[0], ycoord[0]])
 






