

strs = ["flower","flow","flight", "flowerpot"]

def longestCommonPrefix(strs: list[str]) -> str:

	#find shortest string in list
	shortestStr = strs[0]
	for s in strs:
		if len(s) < len(shortestStr):
			shortestStr = s
		else:
			pass
	shortestLen = len(shortestStr)

	#find all prefixes in the shortest string
	prefixes = [shortestStr[0]]
	i = 0
	while i in range(shortestLen - 1):
		prefixes.append(prefixes[i] + shortestStr[1 + i])
		i += 1
		print(prefixes)

	#checks all strings for matching prefixes
	j = 0
	longestCommonPrefix = ""
	for s in strs:
		while j in range(len(s)):
			if longestCommonPrefix + s[j] in prefixes:
				longestCommonPrefix += s[j]
			j += 1






longestCommonPrefix(strs)
