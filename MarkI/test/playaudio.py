
import urllib.request
from pydub import AudioSegment
from pydub.playback import play# Download an audio file


# urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")# Load into PyDub
loop = AudioSegment.from_mp3("speech.mp3")# Play the result

play(loop)