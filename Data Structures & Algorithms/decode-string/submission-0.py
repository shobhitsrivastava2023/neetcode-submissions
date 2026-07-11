class Solution:
    def decodeString(self, s: str) -> str:
        stackstring = ""

        for ch in s:
            if ch != "]":
                stackstring += ch
            else:
                # Step 1: Get characters between ']' and '['
                temp = ""
                while stackstring and stackstring[-1] != '[':
                    temp = stackstring[-1] + temp
                    stackstring = stackstring[:-1]

                # Remove the '['
                if stackstring and stackstring[-1] == '[':
                    stackstring = stackstring[:-1]

                # Step 2: Get the number (could be multiple digits)
                num = ""
                while stackstring and stackstring[-1].isdigit():
                    num = stackstring[-1] + num
                    stackstring = stackstring[:-1]

                # Step 3: Repeat and add back to stackstring
                repeated = int(num) * temp
                stackstring += repeated

        return stackstring

        