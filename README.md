# graph-paths

A simple algorithm to find the total number of paths, given a starting / ending point and a graph.

## Node:

The `Node` class contains its name and a list of all the nodes it is connected to. By creating many nodes and using `node.add_connection()`, we can create a graph of linked nodes.

## Graph:

The `Graph` class stores a starting and an ending point. This helps us keep track of the state of the graph, and also organizes our code.

## Recursion:

This algorithm uses `recursion`. Recursion is basically calling a **function within itself**. It allows use the **same code** over and over again, but with different inputs.

## Explanation:

We start with the starting node. By using a `for loop`, we can get all the connections it has. Then, for each of the nodes, we check two things:

Is the connection the **ending node**? If so, that means we've reached the end of the path. Thus, we will add 1 to the counter, as we have found a valid path.

Have we already passed through that node? If we have, then we are **tracing back on a path we have already taken**, so we continue without checking that path.

If _none_ of those occur, then that means we haven't reached the end of the path yet. We then call the same function, but this time with the **connection** node. This means we will go _one layer deeper_ into the tree of paths, and we _repeat the same process again_.
Once we are done with that, we return the number of **valid paths** we have found, in order to add it to the total.
That's it! We're done!
