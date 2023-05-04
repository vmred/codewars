class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


items = []

items += [Item('+5 Dexterity Vest', 10, 20)]
items += [Item('Aged Brie', 2, 0)]
items += [Item('Elixir of the Mongoose', 5, 7)]
items += [Item('Sulfuras, Hand of Ragnaros', 0, 80)]
items += [Item('Backstage passes to a TAFKAL80ETC concert', 15, 20)]
items += [Item('Conjured Mana Cake', 3, 6)]
items += [Item('Conjured Goblin Axe +1', 4, 16)]


def update_quality():
    for _, v in enumerate(items):
        if 'Sulfuras' not in v.name:
            v.sell_in -= 1

            if 'Backstage' in v.name:
                if v.sell_in <= 0:
                    v.quality = 0
                elif v.sell_in <= 5:
                    v.quality += 3
                elif 5 < v.sell_in <= 10:
                    v.quality += 2
                else:
                    v.quality += 1

            elif 'Aged Brie' in v.name:
                v.quality += 1
            else:
                v.quality -= [1, 2]['Conjured' in v.name]
