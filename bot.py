"""
Actualizaciones:
---------------
Actualmente me logeo, 
voy a una foto con likes y empiezo a seguir a los que le dieron like. Tambien a los seguidores de alguna pagina
Pero me falta escrolear para abajo asi se van cargando los otros botones.

Para dejar de seguir tendria que saber como escrolear hasta abajo y empezar a dejar de seguir de abajo para arriba.

Subir fotos todavia nose.

Tengo que tratar de no entrar y salir mucho a la pagina xq a instagram no le gusta.
"""




from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import os
import time
import random
from random import randint
from os import listdir
from os.path import isfile, join
from InstagramAPI import InstagramAPI
from instapy_cli import client

import sys



def print_same_line(text):
        sys.stdout.write('\r')
        sys.stdout.flush()
        sys.stdout.write(text)
        sys.stdout.flush()


class InstagramBot:




    def __init__(self, username, password):
        
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        
        
        
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.login()
    
    
    def closeBrowser(self):
        self.driver.close()


    def login(self):

        self.driver.get('{}/accounts/login/'.format(self.base_url))

        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element_by_xpath ('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        time.sleep(2)

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))
        
        time.sleep(2)


    def get_inject(self):
        jsFunction = """
        {
            (() => {
                //This getRandomInt function will generate a random pause between performing each action.
	            function getRandomInt(min, max) {
                min = Math.ceil(min);
                max = Math.floor(max);
                return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
	            }

                let i = 0;
                const followInterval = setInterval(() => {
                // Here I set the max amount of followers to 200, you can change that number
                if (i >= 200) {
                clearInterval(followInterval);
                return;
                }
                const buttons = document.getElementsByClassName('sqdOP  L3NKy   y3zKF')
                const nextButton = buttons[i];   // If You want to unfollow from the oldest followed = const nextButton = buttons[400-i];
                nextButton.click();
                window.scrollBy(0, 20)
                i += 1;
                }, getRandomInt(45000,60000))
                // Here at the end ^^^^^^ we have the random miliseconds pause between each action. You can also play with those numbers
            })()

            }
        """
        results = self.driver.execute_script(jsFunction)
        return map(dict,results)

    def follow_user(self, user):
        #self.nav_user(user)
        time.sleep(2)
        
        self.driver.get('{}/explore/tags/animals/'.format(self.base_url))
        time.sleep(2)
        last_picture = self.driver.find_element_by_class_name('eLAPa')
        #//*[@id="react-root"]/section/main/div/div[3]/article[2]/div[1]/div/div[1]/div[1]
        time.sleep(2)
        last_picture.click()
        time.sleep(2)
        self.driver.find_element_by_class_name('_8A5w5').click()
        self.get_inject()

    
        #const followInterval = setInterval(() => {
        """"
        for i in range (1,5):
        
            self.driver.find_elements_by_css_selector("")
            nextButton = buttons[i]
            nextButton.click()
            time.sleep(getRandomInt(30000,60000))
        """
        #follow_button[0].click()
        
        #for i in range (5):
         #   follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[i]
          #  time.sleep(30)
           # follow_button.click()

    def unfollow_user(self, user):
        self.nav_user(user)
     
        unfollow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Following']")[0]
        time.sleep(2)
        unfollow_button.click()

    def like_photos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

         # gathering photos
        pic_hrefs = []
        for i in range(9, 14):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                n = randint(20,30)
                time.sleep(n)
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue


        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1



    
        

if __name__ == '__main__':

    ig_bot = InstagramBot('Fillwithuser','Fillwithpassword')
    time.sleep(2)
    
    ig_bot.follow_user('animals.co')
    
    """
    hashtags = ['animals', 'animales', 'amoranimal', 'vidaanimal', 'animais',
                    'amoanimais', 'animallovers', 'iloveanimals', 'animalslovers', 'animalshots', 'animal_fanatics', 'animal_bestshots',
                    'wildlifeshots', 'wildlife_captures', 'wildlifepictures', 'wildlife_inspired', 'animal_bestshots', 'like4like', 'l4l',
                    'love', 'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy',
                    'dog', 'cat', 'turtle', 'bird', 'lion', 'tiger', 'horse']

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            ig_bot.like_photos(tag)
        except Exception:
            ig_bot.closeBrowser()
            time.sleep(60)
            ig_bot = InstagramBot('dailyanimalsdose','AnimalsDose123!')
            ig_bot.login()
    """
    