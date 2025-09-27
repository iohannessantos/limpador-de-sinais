from flask import Flask as FLASK, render_template, request
app = FLASK(__name__)

@app.route('/', methods=["GET", "POST"]) # GET = buscar dados no servidor, POST = enviar dados ao servidor
def home():
    resultado = ''
    if request.method == 'POST':
        entrada = request.form.get('entrada', '') # Obtém o valor do campo 'entrada' do formulário
        resultado = ''.join([c for c in entrada if c.isdigit()]) # Mantém apenas os dígitos
    return render_template('index.html', resultado=resultado) # Renderiza o template HTML e passa o resultado para ele

if __name__ == '__main__': # Executa o aplicativo Flask
    app.run(debug=True) # Modo debug para reiniciar automaticamente o servidor em caso de mudanças no código


