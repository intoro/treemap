class MockDBHelper:

  def connect(self, database="crimemap"):
    pass

  def get_all_inputs(self):
    return []

  def add_input(self, data):
    pass

  def clear_all(self):
    pass

  def add_tree(self, category, date, latitude, longitude, description):
    pass

  def get_all_trees(self):
    return [{ 'latitude': 33.7722866,
       'longitude': -118.1648778,
       'date': "2000-01-01",
       'category': "mugging",
       'description': "mock description" }]
