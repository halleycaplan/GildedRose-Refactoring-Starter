# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase): # tests each item
    def test_Brie(self):
        items = [Item("Aged Brie", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)
    def test_Sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 2, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)
    def test_Elixir(self):
        items = [Item("Elixir of the Mongoose", 3, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(44, items[0].quality)
    def test_BackStage(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
    def test_Conjured(self):
        items = [Item("Conjured Mana Cake", 0, 8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].quality)



        
if __name__ == '__main__':
    unittest.main()
