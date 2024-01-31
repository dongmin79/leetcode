class Solution:
    def solution(self, ransom_note, magazine):
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransom_note:
            ransom_count[ord(c) - ord('a')] += 1
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        print(ransom_count)
        print(magazine_count)
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))


if __name__ == '__main__':
    print(Solution().solution(ransom_note="aa", magazine="aab"))
