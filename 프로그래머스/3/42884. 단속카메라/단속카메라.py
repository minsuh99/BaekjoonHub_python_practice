def solution(routes):
    routes.sort(key=lambda x: x[1])
    cameras = 1
    camera_pos = routes[0][1]

    for entry, exit in routes:
        if entry > camera_pos:
            cameras += 1
            camera_pos = exit

    return cameras