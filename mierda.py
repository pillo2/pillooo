
import os
import webbrowser

def limpiardns():
    input("presiones una tecla para limliar dns")
    os.system('ipconfig /flushdns')
    webbrowser.register('chrome',None, webbrowser.GenericBrowser(
        'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
    navegador = webbrowser.get("chrome")
    navegador.open_new_tab("htt://chrome://net-internals/#dns")
    



    """os.system('python -m webbrowser -t "chrome://net-internals/#dns')"""


limpiardns()    