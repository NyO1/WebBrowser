# Importa tutte le classi della libreria per costruire GUI con Qt
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *     # Per importare QWebView
from PyQt4.QtCore import *       # Per importare QUrl

app = QApplication([])      # Crea un'applicazione Qt
window = QWidget()          # Crea una finestra (ma non e' visibile)
window.resize(500, 300)     # Imposta dimensione e titolo della finestra
window.setWindowTitle('My Python Web Browser')
layout = QVBoxLayout()      # Crea il layout per la finestra
tlayout = QHBoxLayout()     # Crea il layout per la toolbar
text_bar = QLineEdit('')            # Crea la navigation bar 
button_back = QPushButton('<')      # Crea i bottoni indietro e avanti
button_forward = QPushButton('>')
progress_bar = QProgressBar()       # Crea la progress bar
progress_bar.setMaximumWidth(25)    # Imposta la massima larghezza della progress bar
tlayout.addWidget(button_back)      # Li aggiunge alla toolbar
tlayout.addWidget(button_forward)
tlayout.addWidget(text_bar)
tlayout.addWidget(progress_bar)
web_view = QWebView()       # Crea un widget per visualizzare pagine web
layout.addLayout(tlayout)   # Aggiunge il layout della toolbar a quello della finestra
layout.addWidget(web_view)  # Aggiunge al layout della finestra
window.setLayout(layout)    # Imposta il layout della finestra

def load_page():    # La callback per caricare una pagina
    if text_bar.text() == web_view.url().toString():
        return
    text = str(text_bar.text())
    if ' ' in text or '.' not in text:
        text = 'http://google.com/search?q='+'+'.join(text.split())
    elif '://' not in text:
        text = 'http://'+text
    web_view.setUrl(QUrl(text))

def set_url():     # La callback per immettere il nuovo url nella navigation bar
    text_bar.setText(web_view.url().toString())

# Imposta la callback della navigation bar in risposta all'evento returnPressed 
text_bar.returnPressed.connect(load_page) 
# Imposta la callback della web_view in risposta all'evento urlChanged
web_view.urlChanged.connect(set_url)
# Imposta le callback dei due bottoni in risposta all'evento clicked 
button_back.clicked.connect(web_view.back)
button_forward.clicked.connect(web_view.forward)
# Imposta la callback della web_view in risposta all'evento loadStarted
web_view.loadStarted.connect(progress_bar.reset)
# Imposta la callback della web_view in risposta all'evento loadProgress
web_view.loadProgress.connect(progress_bar.setValue)
# Imposta la callback della web_view in risposta all'evento loadFinished
web_view.loadFinished.connect(progress_bar.reset)
window.show()               # Mostra la finestra
app.exec_()                 # Lancia l'interazione con l'utente