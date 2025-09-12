class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        curr = head
        
        # store references to nodes, not just values
        while curr:
            nodes.append(curr)
            print(curr)
            curr = curr.next
        
        n = len(nodes) // 2
        return nodes[n]
