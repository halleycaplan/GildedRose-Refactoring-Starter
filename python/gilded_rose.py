# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if 10 >= item.sell_in > 5:
                    item.quality = item.quality + 2
                elif 5 >= item.sell_in > 0:
                    item.quality = item.quality + 3
                elif item.sell_in <= 0:
                    item.quality = 0
                else:
                    item.quality = item.quality + 1
                item.sell_in = item.sell_in - 1
            
            elif item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 0:
                    item.quality = item.quality - item.quality
            
            elif item.name == "Conjured Mana Cake":
                if item.quality > 2:
                    item.quality = item.quality - 2
                    item.sell_in = item.sell_in - 1
                elif item.quality < 50:
                    if item.sell_in < 11:
                        item.quality = item.quality + 1
                else:
                    item.quality = 0
 
            elif item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80

            else:
                if item.quality > 0:
                    item.quality = item.quality - 1
                    item.sell_in = item.sell_in - 1
                elif item.quality < 50:
                    if item.sell_in < 11:
                        item.quality = item.quality + 1


        
                


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
