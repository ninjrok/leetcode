class Solution:
    def isEmptyBasket(self, basket):
        return True if len(basket) == 0 else False
    
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        
        baskets = [[], []]
        cont_seq = []
        trials = []
        
        for idx, fruit in enumerate(tree):            
            if fruit in baskets[0]:
                baskets[0].append(fruit)
            elif fruit in baskets[1]:
                baskets[1].append(fruit)
            elif self.isEmptyBasket(baskets[0]):
                baskets[0].append(fruit)
            elif self.isEmptyBasket(baskets[1]):
                baskets[1].append(fruit)
            else:
                trials.append(len(baskets[0]) + len(baskets[1]))
                baskets[0] = cont_seq
                baskets[1] = [fruit]
                # print(trials)
                
            if self.isEmptyBasket(cont_seq):
                cont_seq.append(fruit)
            else:
                if cont_seq[-1] != fruit:
                    cont_seq = []
                cont_seq.append(fruit)
                
            # print(baskets)
                
        trials.append(len(baskets[0]) + len(baskets[1]))
        
        return max(trials)
