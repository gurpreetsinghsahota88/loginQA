#web driver file lauch the webdriver
from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

########## pytest html report ###########
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module data'] = 'Customer'
    config._metadata['Tester'] = 'Gurpreet'

############# It is hook for delete/Modify Enciorment info to HTML Report#########
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

