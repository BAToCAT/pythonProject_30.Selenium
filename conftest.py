import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')
    pytest.driver.get("https://petfriends.skillfactory.ru/login")
    pytest.driver.maximize_window()
    yield

    pytest.driver.save_screenshot('result.png')
    pytest.driver.quit()



def test_show_my_pets():

    WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.ID, "email")))

    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.find_element(By.CSS_SELECTOR, '#navbarNav > ul > li:nth-child(1) > a').click()
    # time.sleep(3)
    pytest.driver.save_screenshot('result.png')

def test_list_of_pets():
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.find_element(By.CSS_SELECTOR, '#navbarNav > ul > li:nth-child(1) > a').click()
    pets = pytest.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]').text


    assert list(pets[17]) == ['3']

def test_pets_info():
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.find_element(By.CSS_SELECTOR, '#navbarNav > ul > li:nth-child(1) > a').click()

    all_my_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr')

    assert len(all_my_pets) > 0

    pets_info = []
    for i in range(len(all_my_pets)):
       pet_info = all_my_pets[i].text
       pet_info = pet_info.split("\n")[0]
       pets_info.append(pet_info)

def test_all_pets_get_photo():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.find_element(By.CSS_SELECTOR, '#navbarNav > ul > li:nth-child(1) > a').click()

    all_pets_images = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr/th/img')

    for i in range(len(all_pets_images)):
        assert all_pets_images[i].get_attribute('src') != ''

def test_names():
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "navbarNav")))
    pytest.driver.find_element(By.CSS_SELECTOR, '#navbarNav > ul > li:nth-child(1) > a').click()

    names = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(2)')

    assert len(names) == 3

    pets_names = []
    for i in range(len(names)):
        pets_name = names[i].text
        pets_name = pets_name.split("\n")[0]
        pets_names.append(pets_name)

    for i in range(len(names)):
        assert names[i] != ' '
        assert names[i] != 'None'
        assert pets_names[0] != pets_names[1]
        assert pets_names[0] != pets_names[2]
        assert pets_names[1] != pets_names[2]


def test_name_descr_age():
    # В моём случае тест падает из-за поля породы - "None"
    # Тест упадет если питомцы добавятся
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Прописано неявное ожидание
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.ID, "navbarNav")

    pytest.driver.find_element(By.CSS_SELECTOR, '#navbarNav > ul > li:nth-child(1) > a').click()

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > th > img')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(2)')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(3)')

    for i in range(len(images)):
        assert images[i].get_attribute('src') != ''
    assert len(names) == 3

    pets_names = []
    for i in range(len(names)):
        pets_name = names[i].text
        pets_name = pets_name.split("\n")[0]
        pets_names.append(pets_name)

    pets_description = []
    for i in range(len(descriptions)):
        pets_desc = descriptions[i].text
        pets_desc = pets_desc.split("\n")[0]
        pets_description.append(pets_desc)
        for i in range(len(pets_description)):
            assert pets_description[i] != 'None'



