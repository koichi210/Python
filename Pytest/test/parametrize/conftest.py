import pytest
 
@pytest.fixture
def promise():

    print('\nInitialize. setup method')

    # execute test
    yield

    print('\nTerminate. teardown method\n')
