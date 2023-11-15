from GraphClass import Graph


def main():
    graph1 = Graph()
    graph1.add_edge("a", "d")
    graph1.add_edge("a", "f")
    graph1.add_edge("b", "c")
    graph1.add_edge("c", "b")
    graph1.add_edge("c", "c")
    graph1.add_edge("c", "d")
    graph1.add_edge("c", "e")
    graph1.add_edge("d", "a")
    graph1.add_edge("d", "c")
    graph1.add_edge("e", "c")
    graph1.add_edge("f", "a")
    graph1.add_edge("z", "z")
    print(graph1)

    print(graph1.bfs_traversal("a"))
    print(graph1.dfs_traversal("a"))

    graph2 = {"a": ["d", "f"],
              "b": ["c", "b"],
              "c": ["b", "c", "d", "e"],
              "d": ["a", "c"],
              "e": ["c"],
              "f": ["a"]
              }

    # print("Hello World")


if __name__ == "__main__":
    main()
