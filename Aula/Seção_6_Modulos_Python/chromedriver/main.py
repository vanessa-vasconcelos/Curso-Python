from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    # Esta linha cria um objeto ChromeOptions, que permite 
    # configurar o navegador com diferentes opções 
    # (como abrir em modo headless, desativar notificações, etc.).
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless') - não exibe navegad.
    
    # ele verifica se foram passadas opções para a função.
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    # Cria a instância do navegador Chrome com o serviço configurado
    # (chrome_service) e as opções adicionadas (chrome_options).
    browser = webdriver.Chrome(
        options=chrome_options
    )

    # Retorna a instância do navegador Chrome, pronta para ser 
    # usada na automação.
    return browser


if __name__ == '__main__':
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    # Aqui, o navegador Chrome é iniciado utilizando a função 
    # make_chrome_browser que foi definida anteriormente. 
    # A função aceita múltiplos argumentos de opções, e aqui 
    # estamos passando as opções da tupla options (neste caso,
    # não há opções extras, pois options é uma tupla vazia).
    browser = make_chrome_browser(*options)

    # Esta linha faz com que o navegador aberto (o objeto browser) 
    # acesse o site do Google. O método get() é utilizado para 
    # carregar uma página da web.
    browser.get('https://www.google.com')

    # Dorme por 10 segundos
    sleep(10)