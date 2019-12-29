from typing import List
import math

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        N = len(books)
        dpH = [math.inf] * (N + 1) # dpH[i] = min total height when i books are placed
        dpH[0] = 0
        for bc in range(1, N + 1):
            i = bc - 1
            remainW = shelf_width
            lvlH = 0
            while i >= 0 and remainW >= books[i][0]:
                remainW -= books[i][0]
                lvlH = max(lvlH, books[i][1])
                dpH[bc] = min(dpH[bc], dpH[i] + lvlH)
                i -= 1
        return dpH[N]

sol = Solution()
ret = sol.minHeightShelves([[12,48],[106,14],[129,108],[76,194],[139,104],[52,20],[145,57],[2,183],[86,96],[42,60],[120,198],[185,80],[139,177],[132,115],[9,21],[105,98],[6,97],[24,136],[163,144],[75,152],[30,76],[127,17],[181,40],[99,6],[39,169],[164,38],[90,56],[10,81],[49,37],[188,103],[37,177],[40,100],[18,6],[9,48],[20,174],[140,119],[34,87],[78,99],[166,174],[106,127],[17,7],[128,138],[170,50],[134,149],[138,85],[14,62],[99,95],[81,21],[20,169],[115,121],[129,2],[114,88],[164,184],[11,168],[111,68],[193,31],[117,132],[154,2],[99,143],[88,62],[56,106],[87,67],[137,51],[67,159],[156,184],[19,47],[116,53],[3,144],[116,175],[111,13],[79,110],[200,100],[117,162],[8,70],[171,182],[125,183],[9,200],[44,131],[65,30],[50,86],[118,111],[149,35],[41,199],[29,74],[10,161],[3,115],[134,76],[126,31],[19,52],[103,130],[95,164],[46,15],[3,100],[37,23],[128,195],[182,151],[111,88],[186,5],[152,92],[22,133],[91,60],[80,120],[51,39],[74,3],[52,45],[168,76],[61,79],[54,60],[143,108],[92,167],[57,182],[173,99],[79,56],[103,3],[112,167],[111,3],[127,83],[51,8],[7,155],[177,42],[181,48],[120,96],[93,1],[78,133],[94,53],[177,173],[110,62],[118,161],[162,42],[137,164],[171,197],[95,143],[44,33],[80,164],[127,4],[86,63],[56,12],[80,39],[145,46],[28,111],[179,79],[162,91],[42,153],[178,13],[14,75],[152,53],[110,159],[11,6],[17,157],[60,170],[174,53],[41,94],[67,34],[147,39],[194,181],[59,77],[29,170],[59,85],[45,74],[94,113],[191,7],[195,6],[184,113],[133,29],[166,129],[198,1],[91,29],[104,166],[74,105],[162,50],[194,151],[22,12],[69,156],[144,92],[94,161],[69,184],[8,139],[200,105],[26,8],[133,111],[76,163],[178,78],[143,198],[106,87],[109,26],[10,105],[37,172],[4,180],[200,69],[137,154],[186,152],[127,4],[104,54],[157,39],[142,170],[50,86],[166,110],[16,101],[195,3],[164,123],[11,105],[152,31],[11,29],[80,93],[113,16],[24,119],[135,95],[161,196],[131,141],[42,188],[169,73],[168,120],[182,87],[173,21],[128,167],[115,160],[160,95],[187,63],[158,52],[146,155],[137,152],[115,107],[48,169],[185,119],[100,187],[17,25],[189,43],[167,109],[168,100],[192,200],[175,112],[145,142],[89,105],[42,163],[150,41],[62,50],[2,43],[80,167],[178,142],[160,168],[1,34],[130,46],[133,185],[141,44],[106,173],[40,55],[168,142],[26,44],[47,187],[145,126],[128,128],[75,34],[154,181],[156,15],[59,102],[12,117],[65,122],[58,60],[193,22],[72,15],[111,10],[123,65],[47,78],[120,176],[186,141],[10,185],[19,179],[30,176],[165,122],[27,199],[68,141],[149,67],[67,113],[106,21],[69,29]],200)            
print(ret)