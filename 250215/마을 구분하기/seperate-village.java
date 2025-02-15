import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static final int MAX_NUM = 100;
    public static int DIR_NUM = 4;
    public static int n;
    public static int[][] grid = new int[MAX_NUM][MAX_NUM];
    public static boolean[][] visited = new boolean[MAX_NUM][MAX_NUM];
    public static ArrayList<Integer> peopleNums = new ArrayList<>();
    public static int peopleNum;
    public static final int[] dxs = new int[]{1, -1, 0, 0};
    public static final int[] dys = new int[]{0, 0, 1, -1};
    
    public static void DFS(int curX, int curY) {
        for(int i = 0; i < DIR_NUM; i++) {
            int newX = curX + dxs[i];
            int newY = curY + dys[i];
            if(canGo(newX, newY)) {
                if(grid[newX][newY] == 1 && !visited[newX][newY]) {
                    visited[newX][newY] = true;
                    peopleNum++;
                    DFS(newX, newY);
                }
            }
        }
    }

    public static boolean canGo(int newX, int newY) {
        if(0 <= newX && newX < n && 0 <= newY && newY < n) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);

       n = sc.nextInt();

       for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
            }
       }

       for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1 && !visited[i][j]) {
                    visited[i][j] = true;
                    peopleNum = 1;

                    DFS(i, j);
                    peopleNums.add(peopleNum);
                }
            }
       }

        Collections.sort(peopleNums);

        System.out.println((int) peopleNums.size());
        for(int i = 0; i < (int) peopleNums.size(); i++)
            System.out.println(peopleNums.get(i));
    }
}