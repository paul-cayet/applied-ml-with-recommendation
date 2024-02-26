## Preventing Abuse Using Unsupervised Learning

`LinkedIn` `2020` https://www.youtube.com/watch?v=sFRrFWYNAUI



#### TLDR;
Isolation Forest is used to detect abusive LinkedIn users, code is open-sourced on Github (https://github.com/linkedin/isolation-forest). Similarity based clustering is also presented.


#### Key points
- It is difficult to use supervised learning for anomaly detection (cost of labeling, low signal -> need for a lot of labels, adversarial behaviour -> frequent need for new labels)\
    -> Unsupervised learning is more suited, as long as anomalous behaviour is different from normal user behaviour.
- They use Isolation forests (code on GitHub). A plot of (feature, Isolation forest score) can help visually identify clusters.
- IF can also be used for insider threat detection, ML model monitoring, Payment fraud, ...
- **Other type of algorithm:** Behavioral Graph clustering, by computing user-user Jaccard Similarity (more precisely Ruzicka similarity with TF-idf as weights) over filtered users and content (to make the quadratic similarity computation faster).
- Then Jarvis-Patrick algorithm is used to refine the clustering (we may have spurious connected components with simple similarity threshold clustering) (algorithm is fast, deterministic, automatically determines number of clusters, clusters will not overlap and can be of variable size)
- Finally, heuristics or supervised ML is used to classify between fake accounts, hacked accounts or real accounts.