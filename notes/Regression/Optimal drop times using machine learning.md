## Optimal drop times using machine learning
`Picnic` `2020` https://blog.picnic.nl/the-trade-off-between-efficiency-and-being-on-time-optimizing-drop-times-using-machine-learning-d3f6fb1b0f31

#### TLDR;
A MLP is used to predict duration of a delivery, which is used (with a safety buffer) with a vehicle routing algorithm to increase the number of deliveries per trip.

#### Key points

- Huber loss is used to account for potential outliers
- Delivery duration is predicted using the type of order, wheather, and proxy variables to represent address/runner: address density (~how many floors) + historical drop time of customer.
- A buffer is used to make sure that customers are delivered in a 20 minutes time window. The buffer is slowly decreased while the on-time perforamnce is closely monitored.
