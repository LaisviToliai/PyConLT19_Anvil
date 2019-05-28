from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# for external databases import pymsql

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.refresh()
    
  def add_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
#     alert(self.new_task_box.text, title="New task")
    anvil.server.call('new_task', self.new_task_box.text)
    self.refresh()

  def refresh(self):
    tasks = anvil.server.call('get_tasks')
#     for t in tasks:
#       print(t["title"])
    self.repeating_panel_1.items = tasks
    

