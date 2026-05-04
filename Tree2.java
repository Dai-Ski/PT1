import java.util.*;

public class Tree2 {
    int v;
    List<List<Integer>> adj;

    Tree2(int v) {
        this.v = v;
        adj = new ArrayList<>();
        for (int i = 0; i < v; i++) {
            adj.add(new ArrayList<>());
        }
    }

    void addEdge(int u, int v) {
        // add edge from u to v
        adj.get(u).add(v);
        // add edge from v to u
        adj.get(v).add(u);
    }

    void printGraph() {
        for (int i = 0; i < v; i++) {
            System.out.println(i + "->" + adj.get(i));
        }
    }

    public static void main(String[] args) {
        Tree2 ob = new Tree2(4);
        ob.addEdge(0, 1);
        ob.addEdge(0, 2);
        ob.addEdge(1, 3);
        ob.printGraph();
    }
}