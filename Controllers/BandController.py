from Models.Band import Band

class BandController():
    def __init__(self):
        self.band = Band()


    def get_band(self, id):
        return self.band.get_band(id)

    def get_band_name(self, id):
        band = self.get_band(id)
        return band[1]
