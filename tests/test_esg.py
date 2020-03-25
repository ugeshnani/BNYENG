import configparser
import pytest
import os
from ESGDataMapper import ESGDataMapper


@pytest.fixture
def file_location():
    config = configparser.RawConfigParser()
    config.read('./venv/ConfigFile.properties')
    location = config.get('DataMapperSection', 'files.location')
    return location


@pytest.fixture
def file_count(file_location):
    count = 0
    location = file_location
    for root, dirs, files in os.walk(location):
        for file in files:
            if str(file).endswith(".csv"):
                count += 1
    return count


def test_config_file():
    assert os.path.exists('./Config/ConfigFile.properties')


def test_file_path(file_location):
    assert os.path.exists(file_location)


def test_files_count(file_count, file_location):
    count = 0
    for root, dirs, files in os.walk(file_location):
        for file in files:
            if str(file).endswith(".csv"):
                count += 1
    assert count == file_count


def test_something(file_location):
    result = ESGDataMapper.construct_tree(ESGDataMapper, file_location, 3)
    assert result == 'success'
