class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        postfix = ['', 'Thousand', 'Million', 'Billion']
        below20 = ['', 'One', 'Two', 'Three', 'Four',
                   'Five', 'Six', 'Seven', 'Eight', 'Nine',
                   'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                   'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        below100 = ['', '', 'Twenty', 'Thirty', 'Forty',
                    'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        parts = []
        lvl = 0
        while num > 0:
            cur = num % 1000
            if cur == 0:
                num = int(num / 1000)
                lvl += 1
                continue
            if lvl > 0:
                parts.append(postfix[lvl])
            hundreds = int(cur / 100)
            cur %= 100
            if cur > 0 and cur < 20:
                parts.append(below20[cur])
            elif cur >= 20:
                tens = int(cur / 10)
                cur %= 10
                if cur > 0:
                    parts.append(below20[cur])
                parts.append(below100[tens])
            if hundreds > 0:
                parts.append('Hundred')
                parts.append(below20[hundreds])
            num = int(num / 1000)
            lvl += 1
        parts.reverse()
        return ' '.join(parts)
