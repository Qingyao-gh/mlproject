from mlproject.distance import haversine

def test_distance_type():
    assert type(haversine(0,0,0,0)) == float

def test_distance_valid():
    assert haversine(20,30,20,30) == 0
