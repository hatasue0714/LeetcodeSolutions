class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        actual_emails = []
        for email in emails:
            actual_email = ""
            atmark_idx = email.find("@")
            local = email[:atmark_idx].replace(".", "")
            plus_idx = local.find("+")
            if plus_idx != -1:
                local = local[:plus_idx]
            actual_email = local + email[atmark_idx:]
            print actual_email
            actual_emails.append(actual_email)
        return len(set(actual_emails))
