package src;

import java.io.File;
import java.util.*;

public class Graph {
    private int vertexCt;  // Number of vertices in the graph.
    private int[][] capacity;  // Adjacency  matrix
    private int[][] residual; // residual matrix
    private int[][] edgeCost; // cost of edges in the matrix
    private String graphName;  //The file from which the graph was created.
    private int totalFlow; // total achieved flow
    private int source = 0; // start of all paths
    private int sink = 0; // end of all paths
    private int[] predecessor;
    private int[] cost;

    public Graph(String fileName) {
        this.vertexCt = 0;
        source  = 0;
        sink = 0;
        this.graphName = "";
        makeGraph(fileName);

    }

    /**
     * Method to add an edge
     *
     * @param source      start of edge
     * @param destination end of edge
     * @param cap         capacity of edge
     * @param weight      weight of edge, if any
     * @return edge created
     */
    private boolean addEdge(int source, int destination, int cap, int weight) {
        if (source < 0 || source >= vertexCt) return false;
        if (destination < 0 || destination >= vertexCt) return false;
        capacity[source][destination] = cap;
        residual[source][destination] = cap;
        edgeCost[source][destination] = weight;
        edgeCost[destination][source] = -weight;
        return true;
    }

    /**
     * Method to get a visual of the graph
     *
     * @return the visual
     */
    public String printMatrix(String label, int[][] m) {
        StringBuilder sb = new StringBuilder();
        sb.append("\n " + label+ " \n     ");
        for (int i=0; i < vertexCt; i++)
            sb.append(String.format("%5d", i));
        sb.append("\n");
        for (int i = 0; i < vertexCt; i++) {
            sb.append(String.format("%5d",i));
            for (int j = 0; j < vertexCt; j++) {
                sb.append(String.format("%5d",m[i][j]));
            }
            sb.append("\n");
        }
        return sb.toString();
    }

    /**
     * Method to make the graph
     *
     * @param filename of file containing data
     */
    private void makeGraph(String filename) {
        try {
            graphName = filename;
            System.out.println("\n****Find Flow " + filename);
            Scanner reader = new Scanner(new File(filename));
            vertexCt = reader.nextInt();
            capacity = new int[vertexCt][vertexCt];
            residual = new int[vertexCt][vertexCt];
            edgeCost = new int[vertexCt][vertexCt];
            for (int i = 0; i < vertexCt; i++) {
                for (int j = 0; j < vertexCt; j++) {
                    capacity[i][j] = 0;
                    residual[i][j] = 0;
                    edgeCost[i][j] = 0;
                }
            }

            // If weights, need to grab them from file
            while (reader.hasNextInt()) {
                int v1 = reader.nextInt();
                int v2 = reader.nextInt();
                int cap = reader.nextInt();
                int weight = reader.nextInt();
                if (!addEdge(v1, v2, cap, weight))
                    throw new Exception();
            }

            reader.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        sink = vertexCt - 1;
        System.out.println( printMatrix("Edge Cost" ,edgeCost));
    }
    private boolean hasAugmentingCheapestPath(){
        //clear predecessor array
        predecessor = new int[vertexCt];
        Arrays.fill(predecessor, -1);
        //set costs to high value
        cost = new int[vertexCt];
        //cost at source is 0 but cost everywhere else is infinity
        Arrays.fill(cost, Integer.MAX_VALUE);
        cost[source] = 0;
        //relaxation loop - three nested for loops
        for(int i = 0; i < vertexCt; i++){
            for(int d = 0; d < vertexCt; d++){
                for(int k = 0; k < vertexCt; k++){
                    //check if edge exists and creates cheaper path
                    if(residual[d][k] > 0 && cost[d] != Integer.MAX_VALUE && cost[k] > edgeCost[d][k] + cost[d]){
                        cost[k] = cost[d] + edgeCost[d][k];
                        predecessor[k] = d;
                    }
                }

            }
        }
        //check if there is a path to the target vertex - checks if it ever got to the sink
        return predecessor[sink] != -1;

    }
    private void findWeightedFlow(){
        String path = "";
        int flow = Integer.MAX_VALUE;
        //Show each path you find in order (and the flow and cost of the path)
        while(hasAugmentingCheapestPath()){
            int prev = predecessor[sink];
            int next = sink;
            flow = Integer.MAX_VALUE;
            path = "";
            while(next != source){
                path = prev + " " + path;
                //find the flow
                if(residual[prev][next] < flow){
                    flow = residual[prev][next];

                }
                //update the next
                next = prev;
                prev = predecessor[next];
            }
            path += sink;
            //reset prev and next
            prev = predecessor[sink];
            next = sink;
            while(next != source){
                //update residual
                residual[prev][next] -= flow;
                //update backEdge
                residual[next][prev] += flow;
                //update the next
                next = prev;
                prev = predecessor[next];
            }
            System.out.println("Path: " + path + " Flow: " + flow + " $: " + cost[sink]);
        }
    }
    private void finalEdgeFlow(){
        //Print the final flow (and cost) on each edge
        //go through the matrix and compare the residual which you have updated in findWeightedFlow to the original graph (capacity)
        //essentially comparing the end result of everything after you have updated residual
        for(int i = 0; i < vertexCt; i++){
            for(int j = 0; j < vertexCt; j++){
                //if there was a change to an edge...
                if(capacity[i][j] - residual[i][j] > 0){
                    System.out.println("Flow " + i + " -> " + j + "(" + (capacity[i][j] - residual[i][j]) + ")" + " $ " + edgeCost[i][j]);

                }
            }
        }

    }


    public void minCostMaxFlow(){
        // show original graph
        System.out.println( printMatrix("Capacity", capacity));
        //Show each path you find in order (and the flow and cost of the path)
        findWeightedFlow();
        System.out.println(printMatrix("Residual", residual));
        //Print the final flow (and cost) on each edge
        finalEdgeFlow();
    }

    public static void main(String[] args) {
        String[] files = {"match0.txt", "match1.txt", "match2.txt", "match3.txt", "match4.txt", "match5.txt","match6.txt", "match7.txt", "match8.txt", "match9.txt"};
        for (String fileName : files) {
            Graph graph = new Graph(fileName);
            graph.minCostMaxFlow();
        }
    }
}