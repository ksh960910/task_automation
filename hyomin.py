import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import schedule
import time
from datetime import datetime
# 목표는 4월 19일 00시에 5월 10일 14:00-18:00 예약하기 !
# ID : 20190194
# PW : 9508
# 과제번호 0720211011 입력하고 예약하기 버튼 !

date = input('몇월 며칠인지를 적어주세요♡ (ex : 0515) : ')
month = date[:2]
day = date[2:]

def reserv():
    url = 'http://cmi-lab.snuh.org/eqreserve/index.php?mode=write&date=2021-' + month + '-' + day + '&e_no=8'
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get(url)
    driver.switch_to.frame(driver.find_element_by_css_selector('html > frameset > frame:nth-child(2)'))
    id = driver.find_element_by_name('u_id').send_keys('20190194')
    pw = driver.find_element_by_name('u_pass').send_keys('9508')

    reserve_time = Select(driver.find_element_by_css_selector('#r_time_h'))
    reserve_time.select_by_visible_text('14')

    reserve_min = Select(driver.find_element_by_css_selector('#r_time_m'))
    reserve_min.select_by_visible_text('0')

    work_hour = Select(driver.find_element_by_css_selector('#r_dur_h'))
    work_hour.select_by_visible_text('4')

    subject_num = driver.find_element_by_css_selector('#r_subject_no').send_keys('0720211011')
    ok_btn = driver.find_element_by_css_selector('#ok_button').click()

schedule.every().day.at('00:00').do(reserv)

while True:
    schedule.run_pending()
    time.sleep(1)