class Solution:
	def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
		A=sorted([[intervals,i] for i,intervals in enumerate(intervals)])
		def find(end):
			l,r=0,len(A)-1
			res=-1
			while l<=r:
				mid=l+(r-l)//2
				if A[mid][0][0]>=end:
					res=A[mid][1]
					r=mid-1
				else:
					l=mid+1
			return res
		res=[]
		for start,end in intervals:
			res.append(find(end))
		return res
