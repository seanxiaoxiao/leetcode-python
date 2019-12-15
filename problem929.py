from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            normalized_email = self.normalizeEmail(email)
            email_set.add(normalized_email)
        return len(email_set)


    def normalizeEmail(self, email) -> str:
        components = email.split("@")
        local_name = components[0].replace(".", "").split("+")[0]
        return local_name + "@" + components[1]