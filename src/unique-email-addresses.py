class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniques = set()
        for email in emails:
            parts = email.split('@')
            plus = parts[0].index('+')
            localName = parts[0][:plus] if plus >= 0 else parts[0]
            localName = localName.replace('.', '')
            uniques.add(localName + '@' + parts[1])
        return len(uniques)
