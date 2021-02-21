# Graph Paths

A simple algorithm to find the total number of paths, given a starting point, ending point, and a graph.

## Explanation:

We start with the starting node. By using a for loop, we can get all the connections it has. Then, for each of the nodes, we check two things:

- Is the connection the ending node? If so, that means we've reached the end of the path. Thus, we will add 1 to the counter, as we have found a valid path.

- Have we already passed through that node? If we have, then we are **tracing back on a path we have already taken**, so we continue without checking that path.

If **none** of those occur, then that means we haven't reached the end of the path yet. We then call the same function, but this time with the connected node. This means we will go one layer deeper into the tree of paths, and we **repeat the same process again**.
Once we are done with that, we return the number of valid paths we have found, in order to add it to the total.
