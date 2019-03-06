# import the tools
from selenium import webdriver
from time import sleep

# statement
print('----------')
print('Notice: this bot will going to like all of the posts which IG account you are target at.')
print('----------')

# need to login to your ig account
print('input your instragm account')
print('username:')
un = input()
print('password:')
pw = input()

# the target ig account
print('input the target IG you want to auto-like')
print('https://www.instagram.com/XXXXXXX/')
print('only need to input the IG username')
url = input()

print('let the bot do the rest thing')

# start the bot
browser = webdriver.Chrome()

# goto the login page
browser.get('https://www.instagram.com/accounts/login/')

# get the input tag and auto input the text
username = browser.find_element_by_name('username')
username.send_keys(un)
password = browser.find_element_by_name('password')
password.send_keys(pw)
button_login = browser.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button')
button_login.click()
# logining to the site


sleep(3)
# dismiss the notification for chrome
notnow = browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()
sleep(3)

# redirect to the target page
browser.get('https://www.instagram.com/'+url)
sleep(4)

# click the first post
first_thumbnail = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
first_thumbnail.click()
sleep(4)

# auto next post and click like
next_post = '1'
null = ''
liked, unlike = 0, 0

while next_post is not null:
    if liked>0 or unlike>0:
        next_post.click()
        sleep(5)
    like = browser.find_element_by_xpath('/html/body/div/div/div/article/div/section[1]/span[1]/button/span')
    print(like.get_attribute("aria-label"))
    if like.get_attribute("aria-label")=="讚":  #另一個叫做「收回讚」 
        like.click()
        liked +=1
    else:
        unlike=1
    try:
        next_post = browser.find_element_by_link_text('下一個')
    except :
        next_post = null

# total of the like
print(str(liked)+' Posts Liked!')

# done.
browser.close()
