# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def quantChange(self,item,x,y): #function to decrease quality in regular/conjured objects
        if item.sell_in > 0:
            item.quality = max(0,item.quality - x) 
        elif item.sell_in <= 0:
            item.quality = item.quality - y
            item.sell_in = item.sell_in - 1
    
    def update_quality(self): #parameters for how to change quality
        for item in self.items:
            if item.name == "Backstage passes to a TAFKAL80ETC concert": #edits quality for concerts
                if 10 >= item.sell_in > 5:
                    item.quality = item.quality + 2
                elif 5 >= item.sell_in > 0:
                    item.quality = item.quality + 3
                elif item.sell_in <= 0:
                    item.quality = 0
                else:
                    item.quality = item.quality + 1
                item.sell_in = item.sell_in - 1

            elif item.name == "Aged Brie": # edits quality for Brie
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 0:
                    item.quality = item.quality - item.quality
            
            elif item.name == "Conjured Mana Cake": # edits quality for Conjured
                self.quantChange(item,2,4)
 
            elif item.name == "Sulfuras, Hand of Ragnaros": # keeps quality constant for Sulfuras
                item.quality = 80

            else: # edits quantity for regular items
                self.quantChange(item,1,2)
                 
        



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
