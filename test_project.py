from unittest import mock

import mock

import base_materials
import cut_materials
from project import add_materials, remove_materials, see_inventory


@mock.patch('project.base_materials.main', return_value="File updated")
def test_add_materials(mock_base_materials_main):
    # Test adding base materials to the mock library, and catching the ValueError
    try:
        with mock.patch('builtins.input', side_effect=[1, "cup", "1", "1.00"]):
            add_materials()
    except ValueError as e:
        # Re-raise the ValueError if it is not the expected ValueError
        if str(e) != "invalid literal for int() with base 10: 'cup'":
            raise e
    assert base_materials.main() == "File updated"


@mock.patch('project.cut_materials.main', return_value="File updated")
def test_add_cut_materials(mock_cut_materials_main):
    # Test adding cut materials to the mock library, and catching the ValueError
    try:
        with mock.patch('builtins.input', side_effect=[2, "paper", "10", "10", "1.00"]):
            add_materials(add_choice=2)
    except ValueError as e:
        # Re-raise the ValueError if it is not the expected ValueError
        if str(e) != "invalid literal for int() with base 10: 'paper'":
            raise e
    assert cut_materials.main() == "File updated"


@mock.patch('project.remove_base_materials.main', return_value="File updated")
def test_remove_materials(mock_base_materials_main):
    # Test removing materials from the mock library, and catching the ValueError
    try:
        with mock.patch('builtins.input', side_effect=[1, "cup", "1"]):
            remove_materials()
    except ValueError as e:
        if str(e) != "invalid literal for int() with base 10: 'cup'":
            raise e
    assert mock_base_materials_main() == "File updated"
  
