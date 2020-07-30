import pytest
 
@pytest.fixture
def setup_method(self, method):
    print('Initialize')
    print('method{}'.format(method.__name__))

def teardown_method(self, method):
    print('Terminate')
    print('method{}:'.format(method.__name__))
