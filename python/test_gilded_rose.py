# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_Brie(self):
        items = [Item("Aged Brie", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)
    def test_Sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 2, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(20, items[0].quality)
    def test_Elixir(self):
        items = [Item("Elixir of the Mongoose", 1, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(6, items[0].quality)
    def test_BackStage(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)




        
if __name__ == '__main__':
    unittest.main()
