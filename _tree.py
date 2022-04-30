from typing import List

from _nutrient import Nutrient


class Tree:
    def __init__(self, habitat, scientific_name, common_name, points, height, sun, water, fire, disturbance, michigander):
        self.habitat = habitat
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.points = points
        self.height = height

        self.nutrients: List[Nutrient] = []
        if sun == 1:
            self.nutrients.append(Nutrient.SUN)
        if water == 1:
            self.nutrients.append(Nutrient.WATER)
        if fire == 1:
            self.nutrients.append(Nutrient.FIRE)
        if disturbance == 1:
            self.nutrients.append(Nutrient.DISTURBANCE)

        self.hugs = 0
        self.michigander = 1 if michigander == 1 else 0

    def info(self):
        return self.scientific_name + ' is a ' + self.habitat + '.'

    def get_formatted_info(self):
        return '- {} | ({} pts, {} ft, {}) | requires {}'.format(
            self.common_name,
            self.points,
            self.height,
            self.habitat,
            list(map(lambda nutrient: nutrient.value, self.nutrients))
        )

    # def plant_facts(self): # returns a list of everything to be added to database
    #     return [self.family, self.genus_species, self.common_name, self.physiognomy, self.conservatism, self.wetness]


if __name__ == '__main__':
    tree_def = ['Conifer', 'Abies balsamea', 'balsam fir', 3, 90, 1, 0, 0, 0, 1]
    tree = Tree(*tree_def)
    print(tree.get_formatted_info())
