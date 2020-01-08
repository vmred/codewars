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
    for i in range(len(items)):
        if 'Sulfuras' not in items[i].name:

            items[i].sell_in -= 1

            if 'Backstage' in items[i].name:
                if items[i].sell_in <= 0:
                    items[i].quality = 0
                elif items[i].sell_in <= 5:
                    items[i].quality += 3
                elif 5 < items[i].sell_in <= 10:
                    items[i].quality += 2
                else:
                    items[i].quality += 1

            elif 'Aged Brie' in items[i].name:
                items[i].quality += 1
            else:
                items[i].quality -= [1, 2]['Conjured' in items[i].name]
