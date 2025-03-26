class Solution(object):
    def findMatrix(self, nums):
        """ Canchola cRUZ Fernando
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        vacia=[]
        listaF=[]
        k=0
        for i in nums:
            vacia.append(nums.count(i))
        mayor=max(vacia)
        matriz = [[] for _ in range(mayor)]
        for i in nums:
            for k in range (0, mayor):
                if i not in matriz[k]:
                    matriz[k].append(i)
                    break

        return matriz
        

        print(matriz)
        