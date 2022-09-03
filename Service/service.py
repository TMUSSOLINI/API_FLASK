from DAO.rodoviaDAO import RodoviaDAO


class ServiceRodovia:
    def __init__(self):
        self.rodovia = RodoviaDAO()

    def create_rod(self, rod):
        self.rodovia.create_rodovia(rod)

    def find(self):
        return self.rodovia.find_all()

    def find_id(self, identi):
        return self.rodovia.find_by_id(identi)

    def delete_by_id(self, identi):
        self.rodovia.delete_by_id(identi)

    def update_by_id(self, rod, identi):
        self.rodovia.update_by_id(rod, identi)
