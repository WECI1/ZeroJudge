M, D = map(int, input().split())

print(['普通', '吉', '大吉'][(M * 2 + D) % 3])