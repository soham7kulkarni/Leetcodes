# Approach - we define key and inside key
# We split each log into two parts, identifier and content
# We specify (0, content, identifier) for letter logs
# and (1,) for digit logs meaning return as it is

# TC - O(N)
# SC - O(1)

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Define a custom sort key function
        def sort_key(log: str):
            # Split the log into identifier and content
            identifier, content = log.split(" ", 1)
            # Return a tuple as the sorting key
            # For letter logs, use (0, content, identifier)
            # For digit logs, use (1,) so they maintain original order
            return (0, content, identifier) if content[0].isalpha() else (1,)
        
        # Sort the logs using the custom key
        logs.sort(key=sort_key)
        
        return logs  # Return the sorted logs
        