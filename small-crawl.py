from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException


def crawlPaperFromTheGioiDiDong():
    header = ['Name', 'Rating', 'Comment']
    df = pd.DataFrame(columns=header)
    driver = webdriver.Chrome()
    
    listOfHyperlink = ["https://www.thegioididong.com/dtdd/samsung-galaxy-note-9"]
    index = 1
    
    while listOfHyperlink:
        ele = listOfHyperlink.pop()
        driver.get(ele)
        #time.sleep(1)
        try:
            nameProduct = driver.find_element(
                By.XPATH, '/html/body/section/div[1]/h1').text
            tmp = driver.find_element(
                By.XPATH, '//*[@id="boxRatingCmt"]/div[3]/div[2]/div')

            idx = 1
            while True:
                try:
                    driver.execute_script('ratingCmtList(' + str(idx) + ')')
                    time.sleep(0.3)
                    listComment = driver.find_element(
                        By.XPATH, '//*[@id="boxRatingCmt"]/div[3]/ul')
                    comments = listComment.find_elements(By.CLASS_NAME, "par")
                    for comment in comments:
                        textComment = comment.find_element(
                            By.XPATH, 'div[2]/p/i').text
                        print(textComment)
                        tmp = comment.find_element(By.XPATH, 'div[2]/p/span')
                        rating = len(tmp.find_elements(
                            By.CLASS_NAME, 'iconcom-txtstar'))

                        # to create dataframe
                        df.set_value(index, "Name", nameProduct)
                        df.set_value(index, "Comment", textComment)
                        df.set_value(index, "Rating", rating)
                        index = index + 1
                        #print(nameProduct, textComment, rating)
                    idx = idx + 1
                except:
                    # for button in buttoms:
                    break
        except NoSuchElementException:
            try:
                """ listComment = driver.find_element(
                    By.XPATH, '//*[@id="boxRatingCmt"]/div[3]/ul')
                comments = listComment.find_elements(By.CLASS_NAME, "par")
                for comment in comments:
                    textComment = comment.find_element(
                        By.XPATH, 'div[2]/p/i').text
                    print(textComment)
                    tmp = comment.find_element(By.XPATH, 'div[2]/p/span')
                    rating = len(tmp.find_elements(
                        By.CLASS_NAME, 'iconcom-txtstar'))

                    df.set_value(index, "Name", nameProduct)
                    df.set_value(index, "Comment", textComment)
                    df.set_value(index, "Rating", rating)
                    index = index + 1
                    print(nameProduct, textComment, rating) """
            except:
                pass
        except:
            pass

    driver.close()
    driver.quit()
    return df

print(crawlPaperFromTheGioiDiDong())