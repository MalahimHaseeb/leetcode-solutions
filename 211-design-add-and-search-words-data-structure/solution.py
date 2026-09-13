class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True 

    def search(self, word: str) -> bool:
        
        def dfs(index, current_node) -> bool:
            node = current_node
            
            for i in range(index, len(word)):
                char = word[i]
                
                if char == '.':
                    for child in node:
                        if child != '$' and dfs(i + 1, node[child]):
                            return True
                    return False
                else:
                    if char not in node:
                        return False
                    node = node[char]
                    
            return '$' in node

        return dfs(0, self.trie)
