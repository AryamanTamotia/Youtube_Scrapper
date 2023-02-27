from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Edge()
driver.maximize_window()
link="https://www.youtube.com/@PW-Foundation/videos"
driver.get(link)

try:
    
    vid_details = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-renderer')
    urls = driver.find_elements(By.XPATH,'//*[@id="video-title-link"]')
    thumbnails = driver.find_elements(By.XPATH,'//*[@id="thumbnail"]/yt-image/img')
    titles = driver.find_elements(By.XPATH,'//*[@id="video-title"]')
    views = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')
    times = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[2]')
except:
		driver.quit()

d={}
for i in range(1,6):
    url=urls[i]
    thumbnail=thumbnails[i]
    title=titles[i]
    view=views[i]
    time=times[i]
    dic={"URL":url.get_attribute("href"),"Thumbnail":thumbnail.get_attribute("src"),"Title":title.text, "Views":view.text, "Time":time.text}
    d[len(d)]=dic

df = pd.DataFrame.from_dict(d, orient='index')
df.to_csv('Youtube_Scrapper.csv')
driver.quit()