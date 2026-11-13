class UF:
    # Creating a union find class with a parents list of size N, along with no rank list 
    def __init__(self, N):
        self.parents = list(range(N))

    def union(self, child, parent):
        # This is how we combine two groups by changing the root of the child to the root of the parent, so they now both have the same parent i.e person we are connecting it with.
        self.parents[self.find(child)] = self.find(parent)
    
    # The goal is to find the root of the group containing x 
    def find(self, x):
        # We check if x is its own parent, if it is then we have reached the parent, otherwise we need to find its parent
        if x != self.parents[x]:
            # We recursiveley call the find function to find the parent of this parent until we hit the root. We set self.parent[x] = self.find(parent[x]) because we want to compress the path so that we can find the parent faster on subsequent calls. This is path compression. 
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # Potential union find algorithim.

        # We create our union find for each account
        uf = UF(len(accounts))

        # Creates unions between indexes
        #ex. "johnsmith@mail.com": 0,
        #    "john_newyork@mail.com": 0
        ownership = {}
        # *emails, is telling the interpretor to unpack the item
        # We want to iterate through the list of accounts
        # understanding the variables:
        # i = index
        # _ = "John", name of the person
        # emails = ["johnsmith@mail.com", "john_newyork@mail.com"] ; list of emails associated with one name NOT JOINED YET 
        for i, (_, *emails) in enumerate(accounts):
            # We loop through each email to detect duplicate emails
            for email in emails:
                if email in ownership:
                # If we have seen the email before we need to merge the current account with the previous recorded account. 
                    uf.union(i, ownership[email])
                # Then we record the current account index as the emails owner 
                ownership[email] = i
        
        # Append emails to correct index 
        ans = defaultdict(list)
        # we iterate through the dictionary of emails with it's indexes mapped (owners)
        for email, owner in ownership.items():
            # We want to append each email to the root owner which we found in the UF so we can just use the find function again to find the proper list we want to append it to. 
            ans[uf.find(owner)].append(email)
        # We use a list comprehension to return back everything. We are appending the name along with the list of sorted emails alphabetically 
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]