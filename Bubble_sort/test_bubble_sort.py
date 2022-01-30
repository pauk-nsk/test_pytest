from main import sort_bubble
import pytest

#сортировка целых чисел
def test_int():
    list = [239, 6, 9, -2, 8, 230, 560, 234, 345, 268, 934, -4]
    list_sort = [-4, -2, 6, 8, 9, 230, 234, 239, 268, 345, 560, 934]
    assert sort_bubble(list) == list_sort

#сортировка дробных чисел
def test_float():
    list = [4.9899, 6, 9, 2.768, 8.67, 230, 560, 234.78, 345.768678, 268, 934, 239]
    list_sort = [2.768, 4.9899, 6, 8.67, 9, 230, 234.78, 239, 268, 345.768678, 560, 934]
    assert sort_bubble(list) == list_sort

#сортировка повторяющихся значений
def test_repeat():
    list = [5, 6, 9, 2, 5, 6, 560, 5, 6, 268, 5, 239]
    list_sort = [2, 5, 5, 5, 5, 6, 6, 6, 9, 239, 268, 560]
    assert sort_bubble(list) == list_sort

#неправильный тип данных в исходном списке
def test_type_error():
    list = [4.9899,6,'text',2.768,8.67,230,560,234.78,345.768678,268,934,239]
    with pytest.raises(TypeError):
         sort_bubble(list)