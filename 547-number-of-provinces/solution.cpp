class Solution {
public:

    void dfs(int city,vector<vector<int>>& isConnected, vector<bool>& visited ){
        visited[city] = true;
        for(int nb = 0; nb < isConnected.size(); nb ++){
            if(isConnected[city][nb] == 1 && !visited[nb]){
                dfs(nb, isConnected, visited);
            }
        }
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n,false);

        int provinces = 0;

        for(int i = 0; i < n; i++){
            if(!visited[i]){
                provinces ++;
                dfs(i, isConnected, visited);
            }
        }

        return provinces;
    }
};
