import tkinter as tk

win = tk.Tk() 

e1 = tk.StringVar() # переменная связанная с полем
entry1 = tk.Entry(master=win, textvariable=e1, width=25).pack(side='left', anchor='nw', padx=5, pady=4)

resp = ''  # выводит переменную после написания данных

def button_clck():
    resp = e1.get() # получить ввод
    file = open("d", "w")
    file.write(resp)
    file.close()
    win.destroy()


button = tk.Button(master=win, text='enter http url from cmd', command=button_clck).pack(side='left', anchor='nw', padx=5, pady=2)

win.mainloop()
f1 = open('d')
url = f1.read(10000)
f1.close
from flask import Flask, request, send_file, render_template
import os
import base64

app = Flask(__name__)

# Папка для хранения загруженных файлов
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    # Сохраняем файл на сервере
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Генерируем ссылку для скачивания
    download_link = f'/download/{file.filename}'
    return url + download_link

@app.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(host='localhost', port=7190)
