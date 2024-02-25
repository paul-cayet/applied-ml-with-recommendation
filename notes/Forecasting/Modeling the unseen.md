## Modeling the unseen
`Instacart` `2019` https://tech.instacart.com/modeling-the-unseen-6a51c9a02430

#### TLDR;
They estimate lost demand (demand that would have occured with enough supply) using 2 cascading ML models that model the conversion probability conditionally to the availabilities.


#### Key points

- Lost demand = (Demand with 100% availability) - (Demand with actual availability)\
- Demand is modeled as a sum of conversion probabilities, estimated from the ML models
- Offline metric is AUC, A/B tests are conducted with 100% availability on selected users to validate models.
- **Note:** They say the total demand is estimated by summing over all customer visits, but I don't see why it is not just from the customer that did not converted (because we know some part of the actual demand). Maybe it to keep a user distribution similar to the one from the training data which balances the errors
