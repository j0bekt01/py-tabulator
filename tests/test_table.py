import inspect

import pytest
from pandas import DataFrame
from pydantic import BaseModel
from pytabulator import TableOptions as TableOptionsPydantic
from pytabulator import Tabulator
from pytabulator._table_options_dc import TableOptions as TableOptionsDC

# from pytabulator import TableOptions, Tabulator

# DEPRECATED: Moved to separate test file
"""
def test_table_options():
    # Prepare
    group_by = ["Sex", "Age"]

    # Act
    table_options = TableOptions(group_by=group_by)
    table_options_dict = table_options.to_dict()
    print(table_options_dict)

    # Assert
    assert table_options_dict["groupBy"] == ["Sex", "Age"]
"""


@pytest.fixture
def df() -> DataFrame:
    data = [["Hans", "22"], ["Peter", [23]]]
    return DataFrame(data, columns=["Name", "Age"])


def test_table(df: DataFrame) -> None:
    # Prepare
    table_options = TableOptionsDC(selectable=3)

    # Act
    table = Tabulator(df, table_options=table_options)
    table_dict = table.to_dict()
    print(table_dict)

    # Assert
    assert list(table_dict.keys()) == ["schema", "data", "options"]
    assert isinstance(table_dict["options"], dict)
    assert hasattr(table.table_options, "__dataclass_fields__")


def test_table_pydantic(df: DataFrame) -> None:
    # Prepare
    table_options = TableOptionsPydantic(selectable=3)

    # Act
    table = Tabulator(df, table_options=table_options)
    table_dict = table.to_dict()
    print(table_dict)

    assert isinstance(table.table_options, BaseModel)
    assert list(table_dict.keys()) == ["schema", "data", "options"]
    assert isinstance(table_dict["options"], dict)
