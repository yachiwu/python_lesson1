# read input data
cost = int(input())      # per unit cost
price = int(input())     # per unit price
maxDemand = int(input()) # maximum possible demand
quantity = int(input())  # order quantity

# initialize the expected sales to 0
expSales = 0.0

# for each possible demand value, 
# add min(demand, quantity) * prob 
# into the expected sales
for demand in range(maxDemand + 1):
  prob = float(input())         # the probability for
                                # this amount of demand
								# to be realized

  if demand < quantity:         # take the smaller one
    expSales += prob * demand   # to be multiplied by
  else:                         # the probability
    expSales += prob * quantity
print(expSales)    

# calculate and print the result
profit = expSales * price - quantity * cost 
print(int(profit))