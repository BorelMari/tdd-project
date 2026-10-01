from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): 
        # Maria entra na página principal do app
        self.browser.get(self.live_server_url)

        # Ela nota que o título da página e o cabeçalho mencionam To-Do
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text  
        self.assertIn('To-Do', header_text)

        # Ela é convidada a entrar com um item To-Do imediatamente
        inputbox = self.browser.find_element(By.ID, 'id_new_item')  
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # Ela digita "Estudar testes funcionais" em uma caixa de texto
        inputbox.send_keys('Estudar testes funcionais')

        # Quando ela aperta enter, a página atualiza, e mostra a lista
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Busca a tabela e o input NOVAMENTE na nova página recarregada
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')  
        self.assertIn('1: Estudar testes funcionais', [row.text for row in rows])

        # Ela entra com "Usar modelos para salvar itens"
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Usar modelos para salvar itens')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Busca a tabela NOVAMENTE na página recarregada
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Estudar testes funcionais', [row.text for row in rows])
        self.assertIn('2: Usar modelos para salvar itens', [row.text for row in rows])