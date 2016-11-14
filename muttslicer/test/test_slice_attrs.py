from .elements import Base,Foo,Bar
import unittest
from muttslicer.slicer import Slicer

class TestSliceAttrs(unittest.TestCase):

    def setUp(self):
        self.foo_list = [
            Foo({'a':1}),
            Foo({'b':2}),
            Foo({'c':3}),
        ]

        self.combined_list = [
            Foo({'a':1}),
            Bar(['b',2]),
            Foo({'c':3}),
            Bar(['d',4]),
            Foo({'e':5}),
        ]

    def test_getitem_single_index(self):
        # ARRANGE
        slicer = Slicer(Foo,self.foo_list)

        # ACT
        single_result = slicer[2]

        # ASSERT
        self.assertEqual(len(single_result),1)
        self.assertIsInstance(single_result,Slicer)
        self.assertEqual(single_result.items[0],self.foo_list[2])

    def test_getslice_with_start_stop(self):
        # ARRANGE
        slicer = Slicer(Foo,self.foo_list)

        # ACT
        sliced_result = slicer[0:3]

        # ASSERT
        self.assertEqual(len(sliced_result),len(slicer))
        self.assertIsInstance(sliced_result,Slicer)
        self.assertEqual(sliced_result.items,slicer.items)

    def test_getitem_with_start_stop_step(self):
        # ARRANGE
        slicer = Slicer(Base,self.combined_list)

        # ACT
        sliced_result = slicer[0:5:2]

        # ASSERT
        self.assertEqual(len(sliced_result),3)
        self.assertIsInstance(sliced_result,Slicer)
        for indx in range(0,5,2):
            item = slicer.items[indx]
            self.assertEqual(sliced_result.items.pop(0),item)

    def test_getitem_with_empty_start_stop(self):
        # ARRANGE
        slicer = Slicer(Base,self.combined_list)

        # ACT
        sliced_result = slicer[:]

        # ASSERT
        self.assertEqual(len(sliced_result),len(slicer))
        self.assertIsInstance(sliced_result,Slicer)
        self.assertEqual(sliced_result.items,slicer.items)

    def test_getitem_single_index_and_mutate(self):
        # ARRANGE
        slicer = Slicer(Base,self.combined_list)
        combine_update = {'z':100}

        # ACT
        result = slicer[0].combine(combine_update)

        # ASSERT
        self.assertEqual(result.items[0].data_dict['combine'],[('a',100)])
        self.assertIsNone(slicer.items[2].data_dict.get('combine',None))

    def test_getitem_slice_and_mutate(self):
        # ARRANGE
        slicer = Slicer(Base,self.combined_list)
        merge_update = {'z':100}

        # ACT
        foo_result = slicer[2:5].merge(merge_update)
        bar_result = slicer[0:2].merge(merge_update)

        # ASSERT
        self.assertEqual(len(foo_result),3)
        self.assertEqual(foo_result.items[0].data_dict['z'],100)
        self.assertEqual(foo_result.items[2].data_dict['z'],100)
        self.assertIn('z', bar_result.items[1].data_list)
        self.assertIn(100, bar_result.items[1].data_list)

    # def test_getitem_single_slice_and_mutate(self):
    #     # ARRANGE
    #     slicer = Slicer(Base,self.combined_list)
    #     merge_update = {'z':100}
    #
    #     # ACT
    #     foo_result = slicer[4:].merge(merge_update)
    #     bar_result = slicer[0:2].merge(merge_update)
    #
    #     # ASSERT
    #     self.assertEqual(len(foo_result),3)
    #     self.assertEqual(foo_result.items[0].data_dict['z'],100)
    #     self.assertEqual(foo_result.items[2].data_dict['z'],100)
    #     self.assertIn('z', bar_result.items[1].data_list)
    #     self.assertIn(100, bar_result.items[1].data_list)

