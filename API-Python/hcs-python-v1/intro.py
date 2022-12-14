import os, time, platform

limpar = 'clear' if platform.system() == 'Linux' else 'cls'

def callIntro():
    intro = [
    '      __    __       ___      .______       _______  ____    __    ____      ___      .______       _______ ',
    '     |  |  |  |     /   \     |   _  \     |       \ \   \  /  \  /   /     /   \     |   _  \     |   ____|',
    '     |  |__|  |    /  ^  \    |  |_)  |    |  .--.  | \   \/    \/   /     /  ^  \    |  |_)  |    |  |__   ',
    '     |   __   |   /  /_\  \   |      /     |  |  |  |  \            /     /  /_\  \   |      /     |   __|  ',
    '     |  |  |  |  /  _____  \  |  |\  \----.|    '  '    |   \    /\    /     /  _____  \  |  |\  \----.|  |____ ',
    '     |__|  |__| /__/     \__\ | _| `._____||_______/     \__/  \__/     /__/     \__\ | _| `._____||_______|',
    '                                                                                                            ',
    '       ______   ______   .__   __. .___________..______        ______    __       __                        ',
    '      /      | /  __  \  |  \ |  | |           ||   _  \      /  __  \  |  |     |  |                       ',
    '''     |  ,----'|  |  |  | |   \|  | `---|  |----`|  |_)  |    |  |  |  | |  |     |  |                       ''',
    '     |  |     |  |  |  | |  . `  |     |  |     |      /     |  |  |  | |  |     |  |                       ',
    '''     |  `----.|  `--'  | |  |\   |     |  |     |  |\  \----.|  `--'  | |  `----.|  `----.                  ''',
    '      \______| \______/  |__| \__|     |__|     | _| `._____| \______/  |_______||_______|                  ',
    '                                                                                                            ',
    '          _______.____    ____      _______..___________. _______ .___  ___.                                ',
    '         /       |\   \  /   /     /       ||           ||   ____||   \/   |                                ',
    '        |   (----` \   \/   /     |   (----``---|  |----`|  |__   |  \  /  |                                ',
    '         \   \      \_    _/       \   \        |  |     |   __|  |  |\/|  |                                ',
    '     .----)   |       |  |     .----)   |       |  |     |  |____ |  |  |  |                                ',
    '     |_______/        |__|     |_______/        |__|     |_______||__|  |__|                                ',
    '                                                                                                            ']
    os.system(limpar)
    for i in intro:
        print(str(i))
        time.sleep(0.1)
