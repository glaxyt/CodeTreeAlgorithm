import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static final int MAX_NUM = 1000;
    public static int n, m;

    public static ArrayList<Integer>[] graph = new ArrayList[MAX_NUM + 1];
    public static boolean[] visited = new boolean[MAX_NUM + 1];
    public static int ans = 0;

    public static void DFS(int node) {
        for(int i = 0; i < graph[node].size(); i++) {
            int curNode = graph[node].get(i);
            if(!visited[curNode]) {
                visited[curNode] = true;
                ans++;
                DFS(curNode);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        for(int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        while(m-- > 0) {
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();

            graph[v1].add(v2);
            graph[v2].add(v1);
        }

        visited[1] = true;
        DFS(1);

        System.out.println(ans);
    }
}