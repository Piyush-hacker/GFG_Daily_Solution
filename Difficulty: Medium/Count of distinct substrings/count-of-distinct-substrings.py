class Solution:
    def countSubs(self, s: str) -> int:
        # Suffix Automaton implementation
        class State:
            def __init__(self):
                self.next = {}
                self.link = -1
                self.length = 0

        sam = [State()]
        last = 0

        for c in s:
            cur = len(sam)
            sam.append(State())
            sam[cur].length = sam[last].length + 1

            p = last
            while p != -1 and c not in sam[p].next:
                sam[p].next[c] = cur
                p = sam[p].link

            if p == -1:
                sam[cur].link = 0
            else:
                q = sam[p].next[c]
                if sam[p].length + 1 == sam[q].length:
                    sam[cur].link = q
                else:
                    clone = len(sam)
                    sam.append(State())
                    sam[clone].length = sam[p].length + 1
                    sam[clone].next = sam[q].next.copy()
                    sam[clone].link = sam[q].link

                    while p != -1 and sam[p].next.get(c) == q:
                        sam[p].next[c] = clone
                        p = sam[p].link

                    sam[q].link = sam[cur].link = clone

            last = cur

        # Count distinct substrings
        ans = 0
        for st in sam[1:]:
            ans += st.length - sam[st.link].length

        return ans
