from asciimatics.screen import Screen
from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, Background
import os

from Baume1 import Baume
import cv2
import numpy as np
#pip install -r requirments.txt
#-------------------------------------------------------------------------------Farbdefinition-----------------------------------------------------------------------------------------
COLOUR_BLACK = 0
COLOUR_RED = 1
COLOUR_GREEN = 2
COLOUR_YELLOW = 3
COLOUR_BLUE = 4
COLOUR_MAGENTA = 5
COLOUR_CYAN = 6
COLOUR_WHITE = 7
A_BOLD = 1
A_NORMAL = 2
A_REVERSE = 3
A_UNDERLINE = 4
#-------------------------------------------------------------------------------DASENDE-----------------------------------------------------------------------------------------
def ENDE(screen):
    while True:
        screen.centre("ENDE",14,COLOUR_WHITE)
        screen.centre("Vielen Dank für die Aufmerksamkeit und besonderer Dank geht an",16,COLOUR_WHITE)
        screen.centre("Lars Bergmann der mir in meinem Praktikum größt mögliche Hilfestellung gegeben hat.",17,COLOUR_WHITE)
        screen.centre("Hallo dein Freundliches Skript ist wieder da!",19,COLOUR_GREEN)
        screen.centre("Setz mich doch bitte mit groß Z zurück. DANKE",20,COLOUR_GREEN)
        screen.refresh()
        ev=screen.get_key()
        if ev in (ord('Q'), ord('q')):
            screen.clear()
            return
        elif ev in (ord("Z"),):
            screen.clear()
            main(screen)
        elif ev in (ord("z"),):
            cap = cv2.VideoCapture('RickRollD.mp4')
            if (cap.isOpened()== False):
                print("Error opening video stream or file")
            while(cap.isOpened()):
                    ret, frame = cap.read()# XXX: x
                    if ret == True:
                        cv2.imshow('Frame',frame)
                        if cv2.waitKey(25) & 0xFF == ord('q'):
                            break
                    else:
                        break
            cap.release()
            cv2.destroyAllWindows()
        screen.refresh()

#-------------------------------------------------------------------------------Studi2-----------------------------------------------------------------------------------------
def  STUDI2(screen):
    while True:
        screen.centre("STUDIENGÄNGE",14,COLOUR_WHITE)
        screen.centre("Nach einem, 5 semester dauerndem, Grundstudium kann man in folgenden Themenbereichen eine Vertiefung wählen.",16,COLOUR_WHITE)
        screen.centre("Wirtschaftsinformatik, AngewandteInformatik, MedizinischeInformatik, BioInformatik, MedienInformatik, TechnischeInformatik",17,COLOUR_WHITE)
        screen.centre("Keine Garantie das die liste Vollstädnig ist!",18,COLOUR_WHITE)
        screen.centre("Um weiter zu Machen Drücke F",20,COLOUR_GREEN)
        screen.refresh()
        ev=screen.get_key()
        if ev in (ord('Q'), ord('q')):
            screen.clear()
            return
        elif ev in (ord("F"),ord("f")):
            screen.clear()
            ENDE(screen)
        screen.refresh()

#-------------------------------------------------------------------------------Studi-----------------------------------------------------------------------------------------
def STUDI (screen):
    while True:
        screen.centre("STUDIUM",14,COLOUR_WHITE)
        screen.centre("Das Studium der Informatik umfasst bereiche wie Mathematik, Algorithmik, Softwareentwicklung und Kommunikationstechnik.",16,COLOUR_WHITE)
        screen.centre("Zudem steht BWL auf dem Lehrplan. Um das Grundstudium antreten zu können benötigt man zwingend das Abitur.",17,COLOUR_WHITE)
        screen.centre("Technisches verständnis und vorkentnisse in Mathematik sind sehr hilfreich da das Studium überaus anspruchsvoll ist.",18,COLOUR_WHITE)
        screen.centre("Möchtest du mehr zu Studiengängen wissen?",20,COLOUR_GREEN)
        screen.centre("Drücke J für Ja oder N für Nein",21,COLOUR_GREEN)
        screen.refresh()
        ev=screen.get_key()
        if ev in (ord("Q"),ord("q")):
            screen.clear()
            return
        elif ev in (ord("J"), ord("j")):
            screen.clear()
            STUDI2(screen)
        elif ev in (ord("N"), ord("n")):
            screen.clear()
            ENDE(screen)
        screen.refresh()

#-------------------------------------------------------------------------------Fisy2-----------------------------------------------------------------------------------------
def FISY2(screen):
    while True:
        screen.centre("Wenn benötigt bitte abschreiben",15,COLOUR_WHITE)
        screen.centre("http://www.xenuser.org/misc/erfahrungsbericht-ausbildung-zum-fachinformatiker-fur-systemintegration/",16,COLOUR_WHITE)
        screen.centre("Um weiter zu Machen Drücke F",17,COLOUR_GREEN)
        screen.refresh()
        ev=screen.get_key()
        if ev in (ord('Q'), ord('q')):
            screen.clear()
            return
        elif ev in (ord("F"),ord("f")):
            screen.clear()
            STUDI(screen)
#-------------------------------------------------------------------------------Fisy-----------------------------------------------------------------------------------------

def FISY (screen):
    while True:
        screen.centre(" FACHHINFORMATIKER SYSTEMINTEGRATION" ,14,COLOUR_WHITE)
        screen.centre("Der FachinforatikerSystemintegration betreut Systeme und Netzwerke, er konzipiert diese und hält sie instand bzw. installiert sie.",16,COLOUR_WHITE)
        screen.centre("Um diese Ausbildung antreten zu können benötigt man einen FOR oder FORQ mit einem guten bis sehr guten Notdendurchschnitt.",17,COLOUR_WHITE)
        screen.centre("Die Ausbildung dauert 3 Jahre und ist dual. Der Betriebliche teil umfasst fachbezogene Schulungen und weiterbildungen.",18,COLOUR_WHITE)
        screen.centre("Der Schulische teil umfasst Programmiersprachen und Mathematik, welche man auch im berufsleben oft benötigt.",19,COLOUR_WHITE)
        screen.centre("Möchtest du mehr Über den Beruf des FachinforatikerSystemintegration erfahren?",21,COLOUR_GREEN)
        screen.centre("Drücke J für Ja oder N für Nein",22,COLOUR_GREEN)
        screen.refresh()
        ev=screen.get_key()
        if ev in (ord("Q"),ord("q")):
            screen.clear()
            return
        elif ev in (ord("J"), ord("j")):
            screen.clear()
            FISY2(screen)
        elif ev in (ord("N"), ord("n")):
            screen.clear()
            STUDI(screen)

    screen.refresh()

#-------------------------------------------------------------------------------MeineTötigkeiten2-----------------------------------------------------------------------------------------
def mm (screen):
    while True:
        screen.centre("Meine ersten Tage waren sehr frustrierend, weil die eigen aneignung von",17,COLOUR_WHITE)
        screen.centre("Programmiersprachen sehr anstregend und fehler behaftet ist.",18,COLOUR_WHITE)
        screen.centre("Wie Murphys law besagt, alles was schiefgehen kann wird schiefgehen!",19,COLOUR_WHITE)
        screen.centre("Um weiter zu machen Drücke F",21,COLOUR_GREEN)
        screen.refresh()
        ev=screen.get_key()
        if ev in (ord('Q'), ord('q')):
            screen.clear()
            return
        elif ev in (ord("F"),ord("f")):
            screen.clear()
            FISY(screen)

    screen.refresh()

#-------------------------------------------------------------------------------Firma2-----------------------------------------------------------------------------------------
def Firma2 (screen):
    while True:
        screen.centre("Perfact.de",19,COLOUR_BLUE)
        screen.centre("Um weiter zu machen Drücke F",20,COLOUR_GREEN)
        screen.refresh()
        ev=screen.get_key()
        if ev in (ord('Q'), ord('q')):
            screen.clear()
            return
        elif ev in (ord("F"),ord("f")):

            mein(screen)
        elif ev in (ord("S"),ord("s")):
            cap = cv2.VideoCapture('ASCII matrix AtoZ 4K.mp4')
            if (cap.isOpened()== False):
                print("Error opening video stream or file")
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    cv2.imshow('Frame',frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()
        screen.refresh()

#-------------------------------------------------------------------------------Firma1----------------------------------------------------------------------------------------
def Firma1 (screen):
    while True:
        screen.centre("PERFACT",14,COLOUR_WHITE)
        screen.centre("Die Firma Perfact Innovation wurde 1998 gegründet.",16,COLOUR_WHITE)
        screen.centre("Sie beschäftigt inzwischen 40 Angestellte,und hat Kunden wie Hapaq Loyd oder Spartherm.",17,COLOUR_WHITE)
        screen.centre("Sie bildet FIAE und FISY aus. Die Atmosphäre im Betrieb ist entspannt, jedoch produktiv.",18,COLOUR_WHITE)
        screen.centre("Alle projekte sind Opensource weshalb das allgemeine Betriebssystem Linux Ubuntu ist.",19,COLOUR_WHITE)
        screen.centre("Möchtest du noch mehr zur Firma wissen?",21,COLOUR_GREEN)
        screen.centre("Drücke J für Ja oder N für Nein",22,COLOUR_GREEN)
        screen.refresh()
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            screen.clear()
            return
        elif ev in (ord("J"), ord("j")):
            screen.clear()
            Firma2(screen)
        elif ev in (ord("N"), ord("n")):
            screen.clear()
            mein(screen)

    screen.refresh()

#-------------------------------------------------------------------------------Mein-------------------------------------------------------------------------------------------
def mein(screen):
    while True:
        screen.centre("MEINE TÄTIGKEITEN",14, COLOUR_WHITE)
        screen.centre("Ich habe in meinem Praktikum große überschneidungen mit dem FIAE gehabt, da Perfacts MPA Abteilung sehr viel programmiert.",16,COLOUR_WHITE)
        screen.centre("Im zuge dieser Programmier Übungen ist auch dieses SCRIPT enstanden.",17,COLOUR_WHITE)
        screen.centre("Wenn du B drückst kannst du ein beispiel meiner Übungen sehen.",18,COLOUR_GREEN)
        screen.centre("Wenn du den Code zu diesem Programm sehen möchstest drücke K",19,COLOUR_GREEN)
        screen.centre("Wenn du das Bild nichtmehr sehen möchtest dann drücke ESC",20,COLOUR_GREEN)
        screen.centre("Wie bereits erwähnt war ich in der Abteilung MPA tätig, welche sich um den support bzw. die problembehebung bei Kunden kümmert.",21,COLOUR_WHITE)
        screen.centre("Die Programmier Sprachen mit denen ich mich in meinem Praktikum auseinander gesetzt habe sind:",22,COLOUR_WHITE)
        screen.centre("Python,SQL,HTML,CSS,Javascript",23,COLOUR_WHITE)
        screen.centre("Möchtest du mehr über Meine Tätigkeiten wissen?",25,COLOUR_GREEN)
        screen.centre("Drücke J für Ja oder N für Nein",26,COLOUR_GREEN)
        screen.refresh()
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            screen.clear()
            return
        elif ev in (ord("J"), ord("j")):
            screen.clear()
            mm(screen)
        elif ev in (ord("N"), ord("n")):
            screen.clear()
            FISY(screen)
        elif ev in (ord("B"), ord ("b")):
            screen.clear()
            tree=Baume(10)
            cur_line=27
            for item in tree:
                screen.centre(item.strip(),cur_line,COLOUR_GREEN)
                cur_line+=1
        elif ev in (ord("K"),ord("k")):
            os.system("see test.png")
            screen.refresh()

    screen.refresh()

#-------------------------------------------------------------------------------Intro-------------------------------------------------------------------------------------------
def intro(screen):
    while True:
        screen.centre("INTRO",14,COLOUR_WHITE)
        screen.centre("Ich habe mein Praktikum in einem IT Dienstleistungs Betrieb durchgeführt.",16,COLOUR_WHITE)
        screen.centre("Dieser Betrieb trägt den Namen Perfact Innovation. Die Firma hat ihren Sitz in Herford an der Eupener Straße 32.",17,COLOUR_WHITE)
        screen.centre("In meinem Praktikum habe ich tiefe einblicke in die Berufe des",18,COLOUR_WHITE)
        screen.centre("FachinforatikerSystemintegration(FISY) und des FachinformtikerAnwednungsEntwicklung(FIAE) bekommen.",19,COLOUR_WHITE)
        screen.centre("Möchtest du mehr zur Firma wissen?",21,COLOUR_GREEN)
        screen.centre("Drücke J für Ja oder N für Nein",22,COLOUR_GREEN)
        screen.refresh()
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            screen.clear()
            return
        elif ev in (ord("J"), ord("j")):
            screen.clear()
            Firma1(screen)
        elif ev in (ord("N"), ord("n")):
            screen.clear()
            mein(screen)


        screen.refresh()

#-------------------------------------------------------------------------------DerAnfang-------------------------------------------------------------------------------------
def main(screen):

    while True:
        screen.centre("HALLO ICH BIN DEIN FREUNDLICHES PYTHON SCRIPT, ICH WERDE DICH DURCH DIESE PRÄSENTATION LEITEN.",18,COLOUR_GREEN)
        screen.centre("TO CONTINUE PRESS J",19,COLOUR_GREEN)
        screen.centre("Videos gehen mit q aus",30,COLOUR_CYAN)
        screen.centre("Sollte >>Frame<< ist Bereit aufploppen drücke ein mal ALT+TAB",31,COLOUR_CYAN)
        screen.refresh()
        ev = screen.get_key()
        if ev in (ord("*"),ord ("+")):
            screen.clear()
            return
        elif ev in(ord ("j"), ord("J")):
            screen.clear()
            intro(screen)

        screen.refresh()

if __name__=="__main__":
    Screen.wrapper(main)
    #main(screen)
