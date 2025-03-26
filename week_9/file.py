"""
COCI' 06 Regional#1 Bard

Every evening villagers in a small village gather around a big fire and sing songs.

A prominent member of the community is the bard. Every evening, if the bard is present,
he sings a brand new song that no villager has heard before, and no other song is sung
that night. In the event that the bard is not present, other villagers sing without him
and exchange all songs that they know.
 (NOTE: villagers can only learn a new song from the bard)


Given the list of villagers present for E consecutive evenings, output all villagers
that know all songs sung during that period.

INPUT SPECIFICATION:
    -> first line is an integer N, number of villagers
    -> second line is an integer E, number of evenings
    -> next E lines contain the list of villagers present on each of the E evenings.
    Each line begins with a positive integer K, the number of villagers present that
    evening, followed by K positive integers separated by spaces representing the villagers.

    No villager will appear twice in one night and the bard will
    appear at least once across all nights.

    Villager number 1 is the bard.

OUTPUT SPECIFICATION:
output all villagers that know all songs, including the bard, one integer per line in
ascending order.

Sample Input -1:
4
3
2 1 2
3 2 3 4
3 4 2 1

Sample Output -1:
1
2
4

Sample Input -2:
8
5
4 1 3 5 4
2 5 6
3 6 7 8
2 6 2
4 2 6 8 1

Sample Output -2:
1
2
6
8
"""

n = int(input())
e = int(input())
villagers = set(range(1, n+1))
for _ in range(e):
    villagers &= set(map(int, input().split()[1:]))
print('\n'.join(map(str, sorted(villagers))))