# Voice switching


def set_voice(voice_gender='female'):
    from main import engine

    voices = engine.getProperty('voices')
    if voice_gender == 'male':
        engine.setProperty('voice', voices[0].id)  # Male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Female voice