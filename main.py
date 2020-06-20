def init(agents, debug=False):
  for agent in range(agents):
    agents.create_agent()
  if debug:
    print("(main.py) initialize command successful")
class agents():
  def create_agent():
   