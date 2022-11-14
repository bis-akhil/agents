
class Order:
    def __init__(self,agent_id,buy,price,vol,fulfilled = False):
        self.agent_id = agent_id
        self.buy = buy
        self.price = price
        self.vol = vol
        self.fulfilled = fulfilled
    
    def __str__(self):
        return f'''
        Agent ID: {self.agent_id}, Buy: {self.buy}, Price: {self.price}, Volume: {self.vol}'''