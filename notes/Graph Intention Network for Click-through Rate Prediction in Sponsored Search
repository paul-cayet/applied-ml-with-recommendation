## Graph Intention Network for Click-through Rate Prediction in Sponsored Search
`Alibaba` `2021` https://arxiv.org/abs/2103.16164

#### TLDR;
The Graph Intention Network (GIN) utilizes a co-occurrence commodity graph to improve click-through rate prediction by enriching sparse user behavior data and exploring potential preferences through graph learning and attention mechanisms


#### Key points

- A co-occurence graph is constructed
    * every time a user goes from product A to product B we add 1 to the edge A-B in the co-occurence graph (undirected).
    * That way, we can jump more easily between similar behaviours
- The embeddings of neighboring nodes are computed in 2 steps:
    1. a tree-like structure of node neigbours is created (Fig 3(a))
    2. embeddings are aggregated, from the most outer neighbours to the 1-hop neighbours
- graph attention is used with the aggregated embeddings to create the **intention vector**
- this vector is concatenated with other features and fed into a MLP (w/ ReLU) trained with a Cross entropy loss (predicting the most likely item to be clicked next)
