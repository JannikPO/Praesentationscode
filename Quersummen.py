import argparse
parser = argparse.ArgumentParser()
parser.add_argument("natZahl")
args = parser.parse_args()
def querSum(natZahl):
    querSumme=0
    zahlString = str(natZahl)
    for zifferBuchstabe in zahlString:
        querSumme = querSumme + int(zifferBuchstabe)
    print(querSumme)

querSum(int(args.natZahl))
