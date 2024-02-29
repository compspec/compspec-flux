#!/usr/bin/env python

# This is a singleton example of running the plugin without compspec,
# primarily to test, etc or just generate a node graph.

import json

from compspec_flux.plugin import Plugin


def main():
    # Load data we've generated with IOR
    plugin = Plugin("flux")

    # Generate the cluster graph
    graph = plugin.generate_graph(cluster_name="dinosaur", exclusive=False)
    print(json.dumps(graph, indent=4))


if __name__ == "__main__":
    main()
