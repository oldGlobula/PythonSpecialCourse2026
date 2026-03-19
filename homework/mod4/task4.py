def task4(s: str) -> None:
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    odd_char = ''
    half = ''
    for ch, count in counts.items():
        if count % 2 == 1:
            if odd_char:
                return
            odd_char = ch
        half += ch * (count // 2)
    palindrome = half + odd_char + half[::-1]
    print(palindrome)
