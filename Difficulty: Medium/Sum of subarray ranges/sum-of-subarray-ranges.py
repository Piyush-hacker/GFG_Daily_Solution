class Solution:
    def subarrayRanges(self, arr):
        n=len(arr)
        stack=[]
        prev_smaller=[-1]*n
        next_smaller=[n]*n
        ans=0
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            prev_smaller[i]=stack[-1] if stack else -1
            stack.append(i)
        stack.clear()
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            next_smaller[i]=stack[-1] if stack else n
            stack.append(i)
        stack.clear()
        prev_larger=[-1]*n
        next_larger=[n]*n
        for i in range(n):
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            prev_larger[i]=stack[-1] if stack else -1
            stack.append(i)
        stack.clear()
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            next_larger[i]=stack[-1] if stack else n
            stack.append(i)
        stack.clear()
        for i in range(n):
            l1=i-prev_smaller[i]
            r1=next_smaller[i]-i
            l2=i-prev_larger[i]
            r2=next_larger[i]-i
            ans+=arr[i]*(l2*r2-l1*r1)
        return ans