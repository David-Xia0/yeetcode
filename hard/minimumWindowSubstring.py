from collections import deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        min_window = None
        min_length = n

        t_map = {}
        for letter in t:
            if letter in t_map:
                t_map[letter].append(-1)
            else:
                d = deque()
                d.append(-1)
                t_map[letter] = d

        left = 0

        while left < n and s[left] not in t_map:
            left += 1
        right = left

        while right < n:
            if s[right] in t_map:
                pos = t_map[s[right]].popleft()
                t_map[s[right]].append(right)

                if pos == -1:
                    min_length = right - left + 1
                    min_window = (left, right)
                else:
                    while left == pos and left < right:
                        left += 1
                        if s[left] not in t_map:
                            pos += 1
                        else:
                            first = t_map[s[left]][0]
                            if first != left and first != -1:
                                pos += 1
                    length = right - left + 1
                    if length < min_length:
                        min_length = length
                        min_window = (left, right)
                right += 1
            else:
                right += 1

        for letter in t_map:
            for l in t_map[letter]:
                if l == -1:
                    return ""

        return s[min_window[0]:min_window[1] + 1]

#
#
# def found_target(target_len):
#     return target_len == 0
#
# class Solution(object):
#     def minWindow(self, search_string, target):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         target_letter_counts = collections.Counter(target)
#         start = 0
#         end = 0
#         min_window = ""
#         target_len = len(target)
#
#         for end in range(len(search_string)):
# 		    # If we see a target letter, decrease the total target letter count
#             if target_letter_counts[search_string[end]] > 0:
#                 target_len -= 1
#
#             # Decrease the letter count for the current letter
# 			# If the letter is not a target letter, the count just becomes -ve
#             target_letter_counts[search_string[end]] -= 1
#
# 			# If all letters in the target are found:
#             while found_target(target_len):
#                 window_len = end - start + 1
#                 if not min_window or window_len < len(min_window):
# 					# Note the new minimum window
#                     min_window = search_string[start : end + 1]
#
# 				# Increase the letter count of the current letter
#                 target_letter_counts[search_string[start]] += 1
#
# 				# If all target letters have been seen and now, a target letter is seen with count > 0
# 				# Increase the target length to be found. This will break out of the loop
#                 if target_letter_counts[search_string[start]] > 0:
#                     target_len += 1
#
#                 start+=1
#
#         return min_window
