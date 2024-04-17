from whisper_live.client import TranscriptionClient

client = TranscriptionClient(
    "localhost", "8091", model="small", lang="en", use_vad=False
)

print(client("/mnt/disk1/chris/OpenVoice/resources/source_en-US-Neural2-D.wav"))
