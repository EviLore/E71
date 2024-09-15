# -*- coding: utf-8 -*-
MAX_QUALITY = 50
MIN_QUALITY = 0
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"
INCREASING_QUALITY_ITEMS = {AGED_BRIE, BACKSTAGE}


class GildedRose(object):

    def __init__(self, items):
        self.items = items


    def update_quality(self):
        for item in self.items:
            if item.name == SULFURAS:
                continue
            if item.name not in INCREASING_QUALITY_ITEMS:
                self.decrement_quality(item)
            else:
                if item.quality < MAX_QUALITY:
                    item.quality += 1
                    if item.name == BACKSTAGE:
                        if item.sell_in < 11:
                            self.increment_quality(item)
                        if item.sell_in < 6:
                            self.increment_quality(item)
            item.sell_in -= 1
            if item.sell_in < 0:
                if item.name != AGED_BRIE:
                    if item.name != BACKSTAGE:
                        self.decrement_quality(item)
                    else:
                        item.quality = MIN_QUALITY
                else:
                    self.increment_quality(item)

    def decrement_quality(self, item):
        if item.quality > MIN_QUALITY:
            item.quality -= 1

    def increment_quality(self, item):
        if item.quality < MAX_QUALITY:
            item.quality += 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
