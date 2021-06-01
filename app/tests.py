import pytest

from script import cuboid_calculator
from app import app as flask_app

# Task 1

# Scenario 1

def test_calculations():
    result = cuboid_calculator(4, 9, 12)
    assert result['volume'] == 432, "Result should be 432"
    assert result['surface_area'] == 384, "Result should be 384"
    assert result['sum_of_edge_lengths'] == 100, "Result should be 100"


# Scenario 2

def test_string():
    string_arg = "Four"
    with pytest.raises(ValueError) as excinfo:
        cuboid_calculator(3, string_arg, 6)
    assert str(excinfo.value) == f"could not convert string to float: '{string_arg}'"


# Scenario 3

def test_non_positive():
    # non_positive_arg must be a float
    non_positive_arg = -9.0
    result = cuboid_calculator(non_positive_arg, 1, 1)
    assert result == f'Error: {non_positive_arg} is a non-positive number.'

# Task 2

# Scenario 1

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page_accessible(app, client):
    """
    GIVEN our Flask application
    WHEN the '/' page is requested
    THEN check that a valid response is returned
    """

    response = client.get('/')
    assert response.status_code == 200
    assert b'Simple Cuboid Calculator' in response.data
    assert b'Enter your edges:' in response.data


# Scenario 2

def test_limited_table_size(app, client):
    """
    GIVEN our Flask application
    WHEN the '/' page is requested
    THEN check there are not more than 30 db entries shown
    """

    response = client.get('/')
    assert response.status_code == 200
    result = response.data.decode("utf-8").count('database-row')
    assert result <= 30
    

# Scenario 3

def test_forms(app, client):
    """
    GIVEN our Flask application
    WHEN the input forms are filled
    THEN check that the calulcation results are pushed to the page
    """

    post_response = client.post('/', data=dict(
        input_a='4',
        input_b='9',
        input_c='12'
    ))
    get_response = client.get('/')
    assert b'Volume: 432.0' in get_response.data
    assert b'Surface Area: 384.0' in get_response.data
    assert b'Sum Of Edge Lengths: 100.0' in get_response.data