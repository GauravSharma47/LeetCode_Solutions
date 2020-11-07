class Solution:
    def reformatDate(self, date: str) -> str:
        months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date,month,year=date.split()
        m=months.index(month)+1
        if m<10:
            m='0'+str(m)
        else:
            m=str(m)
        output=year+'-'+m+'-'
        if len(date)==3:
            output+='0'+date[:1]
        else:
            output+=date[:2]
        return output  
