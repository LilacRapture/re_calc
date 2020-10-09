import re_calc.meta_containers as meta_containers
from re_calc.meta_containers import MetaString, MetaFloat
import unittest


class TestMetaContainers(unittest.TestCase):

    def test_MetaString(self):
        base_string = "str"
        meta_data = "some meta"
        string_with_meta = MetaString(base_string, meta_data)
        result = string_with_meta + "!"
        self.assertEqual("str!", result)
        self.assertEqual(meta_data, string_with_meta.meta)
        lst = [string_with_meta]
        lst.append("other element")
        self.assertEqual(meta_data, lst[0].meta)

    def test_MetaFloat(self):
        base_float = 1.0
        meta_data = "some meta"
        float_with_meta = MetaFloat(base_float, meta_data)
        result = float_with_meta + 1.0
        self.assertEqual(2.0, result)
        self.assertEqual(meta_data, float_with_meta.meta)
        lst = [float_with_meta]
        lst.append("other element")
        self.assertEqual(meta_data, lst[0].meta)

    def test_pack(self):
        packed_int = meta_containers.pack(1, "some meta")
        packed_float = meta_containers.pack(1.0, "some meta 2")
        packed_str = meta_containers.pack("str", "some meta 3")
        self.assertTrue(isinstance(packed_int, int))
        self.assertTrue(isinstance(packed_float, MetaFloat))
        self.assertTrue(isinstance(packed_str, MetaString))
        self.assertEqual("some meta 2", packed_float.meta)
        self.assertEqual("some meta 3", packed_str.meta)

    def test_set_meta_indices(self):
        lst = [1, 1.0, "str"]
        [o_int, m_float, m_string] = meta_containers.set_meta_indices(lst)
        self.assertTrue(isinstance(o_int, int))
        self.assertEqual(1, m_float.meta)
        self.assertEqual(2, m_string.meta)

    def test_set_meta_list(self):
        lst = [1, 1.0, "str"]
        result = meta_containers.pack_list(lst, 'string')
        self.assertTrue(isinstance(result, list))
        self.assertEqual('string', result.meta)
