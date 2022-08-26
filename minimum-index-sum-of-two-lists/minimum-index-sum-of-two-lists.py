class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        #print(type(list1[0]))
        
        common = set(list1).intersection(set(list2))
        #print(type(common))
        list1_dict = dict(map(reversed, enumerate(list1)))
        list2_dict = dict(map(reversed, enumerate(list2)))
        
        #print(list1_dict,list2_dict)
        
        min_index_sum = float('inf')
        index_sum ={}
        if len(common) ==1:
            
            return common
        else:
            temp =[]
            for i in common:
                #i = str(i)
                #print('i',type(i))
                index_sum[i] = list1_dict[i]+list2_dict[i]
                
#                 if min_index_sum > min(min_index_sum,(list1_dict[i]+list2_dict[i])):

#                     min_index_sum = min(min_index_sum,(list1_dict[i]+list2_dict[i]))
#                     temp = i
                    
        #temp=(temp)
        
        print(index_sum)
        dict2 = dict([(v, [k for k, v1 in index_sum.items() if v1 == v])
              for v in set(index_sum.values())])
        return(dict2[min(dict2.keys())])
        #values=list(index_sum.values())
        #print(list(index_sum.keys())[values.index(min(values))])
        #return ([temp])
                
        