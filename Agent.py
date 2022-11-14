import numpy as np
from Order import Order


class Agent:
    def __init__(self,agent_id,fund_value, trade_frequency):
        self.trade_frequency = trade_frequency
        self.price_hist = [fund_value]
        self.mid_price_hist = [fund_value]
        self.alpha = 100
        self.agent_id = agent_id
        self.fund_value = fund_value
        
    def consume_data(self,new_data):
        self.price_hist.append(new_data['new_price'])
        self.mid_price_hist.append(new_data['mid_price'])
       
        
    def order_deets(self):
        noise_fund = np.random.normal(0,1)/100
        fund_val = self.fund_value*(1+noise_fund)
        noise_volume = np.random.normal(0,1)/100
        noise_price = np.random.normal(0,1)/100
        volume = self.alpha*(fund_val - self.mid_price_hist[-1])*(1 + noise_volume)
        price = self.mid_price_hist[-1]*(1 + noise_price)
        buy = 1
        if volume<0:
            buy=0
            volume = -volume
        new_order = Order(self.agent_id,buy,price,volume)
        return new_order
    
    def if_order(self):
        prob = self.trade_frequency
        truth = 1 if np.random.random() < prob else 0
        if truth:
            new_order = self.order_deets()
            return new_order
        else:
            return 0

        
    def __str__(self):
        return f"""The agent id is {self.agent_id}"""