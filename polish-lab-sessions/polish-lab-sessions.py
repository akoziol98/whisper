import whisper
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

model = whisper.load_model("small")
#result = model.transcribe("../polish-data/lab-sessions/77003_1_manipulative_kam1.wav")
result = model.transcribe("../polish-data/home-recordings/V20211121-091352.mp3")
print(result["text"])