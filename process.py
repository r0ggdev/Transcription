import subprocess

class Process:

    def join_video(video_path, subtitles_path, output_path):
        command = [
            'ffmpeg',
            '-i', video_path,         # Archivo de entrada (video MKV)
            '-i', subtitles_path,     # Archivo de subtítulos (SRT)
            '-c:v', 'copy',           # Copiar el video sin recodificación
            '-c:a', 'aac',            # Codificar el audio como AAC
            '-c:s', 'mov_text',       # Usar mov_text para subtítulos en MP4
            '-strict', 'experimental', # Usar características experimentales si es necesario
            output_path               # Archivo de salida (MP4)
        ]
    
        subprocess.run(command)

    # join_video('audios/funcionaShazam.mkv', 'subtitles.srt', 'output_video.mp4')

Process.join_video("video.webm","export/output/salida_sub.srt","export/output/salida_video.mp4")
