def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(cur_k, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(len(dungeons)):
            need_k, use_k = dungeons[i]

            if not visited[i] and cur_k >= need_k:
                visited[i] = True
                dfs(cur_k - use_k, count + 1)
                visited[i] = False

    dfs(k, 0)
    return answer