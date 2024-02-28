## Tuning Model Performance

`Uber` `2021` https://eng.uber.com/tuning-model-performance/


#### TLDR;
A few tricks related to model performance tuning / HPO are presented.

#### Key points
- To avoid overfitting with HPO, they **regularize the HPO process** with a “penalty” that captures the difference between training and test performance.
- They use joint information from models learning curves to perform pruning (e.g. using Asynchronous Successive Halving Algorithm on top of sequential Bayesian) (also: see Cubic regularization).
- They use embeddings for geospatial features, and use composite features (I imagine such as x1.x2, ...) (maybe filtered with feature selection step) when using Tree-based models
- Training models accross a large date range improves performance unless it doesn't, in which they apply **time-weighted decay** on the training data.

