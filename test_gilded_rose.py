# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    def test_qualitycantbeover50(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sellinpass(self):
        items = [Item("foo", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(47, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(45, items[0].quality)

    def test_agedbrietraits(self):
        items = [Item("Aged Brie", 1, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(46, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(48, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)


    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(1, items[0].sell_in)
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_backstagepasses(self):
        #"Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
	    #Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
	    #Quality drops to 0 after the concert
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        gilded_rose.update_quality()
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_generic50(self):
        items = [Item("foo", 10, 52)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(51, items[0].quality)



        
if __name__ == '__main__':
    unittest.main()
