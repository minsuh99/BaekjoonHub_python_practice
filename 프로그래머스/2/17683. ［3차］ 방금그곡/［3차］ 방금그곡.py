def replace_melody(melody):
    for tone in ["C#", "D#", "F#", "G#", "A#"]:
        melody = melody.replace(tone, tone[0].lower())
    
    return melody

def solution(m, musicinfos):
    answer = []
    
    for musicinfo in musicinfos:
        start, end, title, info = map(str, musicinfo.split(","))
        
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        
        start = sh * 60 + sm
        end = eh * 60 + em
        playtime = end - start
        
        # 음 대체 작업
        m = replace_melody(m)
        info = replace_melody(info)
        
        target = info * (playtime // len(info)) + info[:playtime % len(info)]
        if m in target:
            answer.append((title, playtime))
    
    answer.sort(key=lambda x:(-x[1]))
    
    
    return "(None)" if not answer else answer[0][0]