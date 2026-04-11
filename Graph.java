public class Graph {
    public static void main(String[] args) {
        int V = 3;
        int[][] matrix = new int[V][V];
        // add edges
        matrix[0][1] = 1;
        matrix[1][0] = 1;

        matrix[1][2] = 1;
        matrix[2][1] = 1;

        // print matrix
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                System.out.println(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}