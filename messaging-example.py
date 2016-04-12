from orderbook import OrderBook
from ordertree import OrderTree
from orderlist import OrderList
from order import Order
import random
import sys

def main():
    
    # TODO: Create three agents:
    order_book = OrderBook()
    agents = [101, 102, 103]

    # TODO: Agents send in buy/sell orders randomly with some probablility
    for i in range(30):
        print '\nTimestep# {}: '.format(i)
        for a in agents:
            if (random.random() > 0.5):
                # make an order
                # buy or sell?
                tradedir = random.choice(['bid','ask'])
                # how many?
                ordqty = random.randint(1,20)
                # market or limit?
                tradetype = random.choice(['market', 'limit'])
                # if limit, what is your bid/ask price
                if tradetype == 'limit':
                    limitprice = random.uniform(90,100)
                # send in the order
                if tradetype == 'market':
                    agent_order = {'type':'market', 'side':tradedir, 'quantity':ordqty, 'trade_id':a}
                    print 'agent {} made a market order to {} {} orders'.format(a, tradedir, ordqty)
                else:
                    agent_order = {'type':'limit', 'side':tradedir, 'quantity':ordqty, 'price':limitprice, 'trade_id':a}
                    print 'agent {} made a limit order at {} to {} {} orders'.format(a, limitprice, tradedir, ordqty)
                
                trades, order_in_book = order_book.process_order(agent_order, False, False)
            else:
                print 'agent {} did not trade'.format(a)
    # plot how the stock changes
    print order_book

if __name__ == "__main__":
    sys.exit(int(main() or 0))