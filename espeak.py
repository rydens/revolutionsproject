import subprocess as sp


def say(text=None,voice=None):
  text = " '" + text + "'"
  if voice != None:
    voice = " -v " + voice
  else:
    voice = ""
  sp.call("espeak" + voice + text, shell=True)

if __name__ == '__main__':
  say("Hi There! This is my eSpeak module.")
