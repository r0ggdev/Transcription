import whisper

class Transcription:

    def __init__(self, _folder, _name, _input):
        self.model = whisper.load_model("turbo")
        self.folder = _folder
        self.name = _name
        self.path = f"{self.folder}/{self.name}"
        self.result = self.model.transcribe(_input)

    def crear_archivo_srt(self):
        srt_filename = f"{self.path}_sub.srt"

        with open(srt_filename, "w", encoding="utf-8") as srt_file:
            for i, segment in enumerate(self.result["segments"]):

                start_time = segment["start"]
                end_time = segment["end"]
                text = segment["text"].strip()

                start_time_str = f"{int(start_time // 3600):02}:{int((start_time % 3600) // 60):02}:{int(start_time % 60):02},{int((start_time % 1) * 1000):03}"
                end_time_str = f"{int(end_time // 3600):02}:{int((end_time % 3600) // 60):02}:{int(end_time % 60):02},{int((end_time % 1) * 1000):03}"

                srt_file.write(f"{i + 1}\n")
                srt_file.write(f"{start_time_str} --> {end_time_str}\n")
                srt_file.write(f"{text}\n\n")

        print(f"Subtítulos guardados en {self.name}_sub")

    def crear_archivo_transcripcion(self):
        transcription_filename = f"{self.path}_text.txt"
        
        with open(transcription_filename, "w", encoding="utf-8") as transcription_file:
            for segment in self.result["segments"]:
                transcription_file.write(segment["text"].strip() + " ")

        print(f"Transcripción guardada en {self.path}_text")


# Ejemplo de uso
transcripcion = Transcription("./export/output/", "salida","video.webm")
transcripcion.crear_archivo_srt()
transcripcion.crear_archivo_transcripcion()
