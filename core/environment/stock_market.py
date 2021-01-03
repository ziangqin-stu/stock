import os
import csv
import data


class BaseMarket:
    def __init__(self, conf):
        # create private data filed
        self.conf = conf
        self.decision_len = conf.decision_len
        self.stock_history = []
        self.capital = conf.capital
        # init private data
        self._load_stock_data(conf.stock_code)
        self.reset()

    def _load_stock_data(self, stock_code):
        # data_names = sorted(glob.glob(os.path.join(data.data_path, '*.csv')))
        data_name = os.path.join(data.data_path, stock_code + '.csv')
        with open(data_name) as f:
            stock_history = []
            f_csv = csv.reader(f)
            for row in f_csv:
                if row[0] != 'Date': stock_history.append(row)
        self.stock_history = [list(map(float, line[1:])) for line in stock_history]

    def _init_agent(self, capital):
        self.agent_state = AttrDict({
            'time': 0,
            'hold': 0.0,
            'money': float(capital)
        })

    def reset(self):
        self._init_agent(self.conf.capital)
        return [i for i in self.agent_state.values()] \
               + self.stock_history[self.agent_state.time: self.agent_state.time + self.decision_len], \
               0, False, {}

    def step(self, action):
        # trade operation
        self.agent_state.hold += action
        self.agent_state.money -= action * self.stock_history[self.agent_state.time][3]
        instant_reward = self.agent_state.money + self.agent_state.hold * self.stock_history[self.agent_state.time][3] \
                         - self.capital
        # update market to next day
        self.agent_state.time += 1
        observation = [i for i in self.agent_state.values()] \
                      + self.stock_history[self.agent_state.time: self.agent_state.time + self.decision_len]
        done = (self.agent_state.time == len(self.stock_history))
        return observation, instant_reward, done, {}

    def render(self):
        pass


if __name__ == "__main__":
    from core.utils.general_util import AttrDict

    conf = AttrDict({
        'decision_len': 90,
        'stock_code': '000001.sz',
        'capital': 100.0
    })
    market = BaseMarket(conf)
    x = market.reset()
    print(x)
    y = market.step(10.0)
    print(y)
