#!/usr/bin/env/python
# -*- coding:utf-8 -*-
__author__ = 'zcy'

import time
from selenium import webdriver


class GetCompanyInfos():

    def __init__(self):
        self.username = 'xxxxxxxxxxxxx'
        self.password = 'xxxxxxxxxxxxx'
        self.driver = webdriver.Firefox()
        self.start_url = 'https://www.tianyancha.com/login?' \
                         'from=https%3A%2F%2Fwww.tianyancha.com%' \
                         '2Fsearch%3Fbase%3Dnanjing'

    # 登录天眼查
    def login(self):
        self.driver.get(self.start_url)
        login_by_pwd = self.driver.find_element_by_xpath(
            'html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]')
        time.sleep(1)
        # 点击以账号密码方式登录
        login_by_pwd.click()
        # 找到账号、密码的输入框
        input1 = self.driver.find_element_by_xpath(
            'html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/input')
        input2 = self.driver.find_element_by_xpath(
            'html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[3]/input')
        time.sleep(2)
        # 输入账号及密码
        input1.send_keys(self.username)
        time.sleep(2)
        input2.send_keys(self.password)
        time.sleep(2)
        # 定位并点击登录按钮
        login_button = self.driver.find_element_by_xpath(
            'html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[5]')
        time.sleep(2)
        login_button.click()
        # 给予10s钟时间加载滑块，并实现滑动登录
        time.sleep(15)
        # 获取当前页面信息
        page = self.driver.page_source
        if page.find('xxxxxxxxxx') != -1:
            print('登录成功')

    # 从文件中读取企业信息
    def get_company_name(self):
        f = open('E:\\documents\\diffClean.txt', 'r', encoding='utf-8')
        lines = f.readlines()
        return lines

    # 获取企业信息
    def get_company_info(self, company_name):
        time.sleep(1)
        # page = self.driver.page_source
        time.sleep(1)
        index_input_company = self.driver.find_element_by_xpath(
            'html/body/div[1]/div/div[2]/div/div[2]/div[1]/form/div/input')
        time.sleep(1)
        index_input_company.clear()
        index_input_company.send_keys(company_name)
        time.sleep(1)
        self.driver.find_element_by_xpath('html/body/div[1]/div/div[2]/div/div[2]/div[1]/div').click()
        # 公司名称
        company_list = self.driver.find_element_by_xpath(
            'html/body/div[2]/div/div[1]/div/div[3]/div/div/div[3]/div[1]/a')
        # 获取搜索公司的链接网址
        href = company_list.get_attribute('href')
        time.sleep(1)
        self.driver.get(href)
        time.sleep(1)
        # 获取搜索公司信息
        company = self.save_company_info()
        return company

    # 保存企业信息
    def save_company_info(self):
        company = ''
        company_name = self.driver.find_element_by_xpath(
            'html/body/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[1]/h1')
        company += '公司名:' + company_name.text + '\t'
        registered_fund = self.driver.find_element_by_xpath(
            'html/body/div[2]/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[2]/div[2]/table[2]/tbody/tr[1]/td[2]/div')
        company += '注册资金:' + registered_fund.text + '\t'
        establishment_date = self.driver.find_element_by_xpath(
            'html/body/div[2]/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[2]/div[2]/table[2]/tbody/tr[1]/td[4]/div')
        company += '成立时间:' + establishment_date.text + '\t'
        contributed_capital = self.driver.find_element_by_xpath(
            'html/body/div[2]/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[2]/div[2]/table[2]/tbody/tr[7]/td[2]')
        company += '实缴资金:' + contributed_capital.text + '\t'
        business_nature = self.driver.find_element_by_xpath(
            'html/body/div[2]/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[2]/div[2]/table[2]/tbody/tr[4]/td[4]')
        company += '公司性质:' + business_nature.text + '\t'
        company_industry = self.driver.find_element_by_xpath(
            'html/body/div[2]/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[2]/div[2]/table[2]/tbody/tr[5]/td[4]')
        company += '所属行业:' + company_industry.text + '\t'
        registered_address = self.driver.find_element_by_xpath(
            'html/body/div[2]/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[2]/div[2]/table[2]/tbody/tr[9]/td[2]')
        company += '注册地址：' + registered_address.text + '\t'
        business_scope = self.driver.find_element_by_xpath(
            'html/body/div[2]/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[2]/div[2]/table[2]/tbody/tr[10]/td[2]'
            '/span/span/span[2]')
        company += '经营范围:' + business_scope.text + '\t'
        patent = self.getPatentInfos()
        company += '知识产权样本:' + patent + '\n'
        return company

    # 获取专利信息改
    def getPatentInfos(self):
        self.driver.find_element_by_xpath('html/body/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div[6]/a').click()
        patent = self.driver.find_element_by_id("nav-main-knowledgeProperty").text
        if str(patent).__contains__("暂无相关信息，看看该公司的其他信息"):
            patent = '该企业暂无专利信息'
            return patent
        else:
            return patent

    # main()方法
    def main(self):
        self.login()
        company_name = self.get_company_name()
        for cn in company_name:
            name = cn.split(',')
            print(name[0])
            company = self.get_company_info(name[0])
            if company == name[0]:
                res = company + '没有相关信息' + '\n'
            else:
                res = company
            output = open('E:\\documents\\company2.txt', 'a', encoding='utf-8')
            output.write(res)
            output.close()
        self.driver.close()


if __name__ == '__main__':
    time1 = time.time()
    new_crawl = GetCompanyInfos()
    new_crawl.main()
    time2 = time.time()
    print('用时:', int(time2 - time1))
