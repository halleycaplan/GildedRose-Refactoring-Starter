# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros":
                if item.quality > 0:
                    item.quality = item.quality - 1
                    item.sell_in = item.sell_in - 1
                elif item.quality < 50:
                    if item.sell_in < 11:
                        item.quality = item.quality + 1
                      
            
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if 10 >= item.sell_in > 5:
                    item.quality = item.quality + 2
                elif 5 >= item.sell_in > 0:
                    item.quality = item.quality + 3
                elif item.sell_in <= 0:
                    item.quality = 0
                else:
                    item.quality = item.quality + 1
                if item.quality > 50:
                    item.quality = 50
                item.sell_in = item.sell_in - 1
            
            elif item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 0:
                    item.quality = item.quality - item.quality

        
                


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
